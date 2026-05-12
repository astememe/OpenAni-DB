import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
## import OpenAni_DB.routing
##### HAY QUE CREAR MODELO CHATCONSUMER (MIRAR LA PAGINA GUIA Y EL GEMINI)
##### HAY QUE CREAR EL ARCHIVO ROUTING.PY DESPUÉS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenAni_DB.settings')

# 1. Inicializamos la aplicación ASGI de Django primero
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # Maneja el HTTP normal (tus interfaces de Retrofit)
    "http": django_asgi_app,

    # Maneja los WebSockets de tu App Android
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})