import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from Messaging.chat_consumers import routing
## import OpenAni_DB.routing
##### HAY QUE CREAR MODELO CHATCONSUMER (MIRAR LA PAGINA GUIA Y EL GEMINI) listo cruck
##### HAY QUE CREAR EL ARCHIVO ROUTING.PY DESPUÉS listo cruck

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenAni_DB.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,

    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})