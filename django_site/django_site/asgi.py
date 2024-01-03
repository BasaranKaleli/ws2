import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from livechat import routing as chat_routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_site.settings")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    chat_routing.websocket_urlpatterns
                )
            )
        ),
    }
)
