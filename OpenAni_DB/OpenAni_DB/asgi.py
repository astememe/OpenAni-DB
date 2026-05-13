import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
## import OpenAni_DB.routing
##### HAY QUE CREAR MODELO CHATCONSUMER (MIRAR LA PAGINA GUIA Y EL GEMINI)
##### HAY QUE CREAR EL ARCHIVO ROUTING.PY DESPUÉS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenAni_DB.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,

    "websocket": AuthMiddlewareStack(
        URLRouter(
            ## chat.routing.websocket_urlpatterns
        )
    ),
})