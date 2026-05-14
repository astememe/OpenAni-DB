# chat/routing.py
from django.urls import re_path
from Messaging.chat_consumers import consumers

websocket_urlpatterns = [
    # Usamos re_path para capturar el group_id de la URL
    # Esta ruta coincide con la que pongas en Android Studio
    # 'ws/chat/(?P<group_id>\w+)/$' -> es un capturador. Lo que está entre <> es el nombre de la variable que se usa en consumers.
    # Hace que se pueda llamar en consumers como: self.group_id = self.scope['url_route']['kwargs']['group_id']
    # w+ -> permita valores alfanuméricos con más de 1 dígito.
    re_path(r'ws/chat/(?P<group_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
