import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model # Importante para usar tu UserModel
from Messaging.models import message_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.room_group_name = f'chat_{self.group_id}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message_text = data['message']
            username = data['sender_username']

            await self.save_message(username, self.group_id, message_text)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message_text,
                    'sender_username': username
                }
            )
        except Exception as e:
            print(f"Error en receive: {e}")

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_username': event['sender_username'],
            'timestamp': "ahora" # Opcional: puedes pasar el tiempo real aquí
        }))

    @database_sync_to_async
    def save_message(self, username, thread_id, text):
        try:
            user = User.objects.get(username=username)
            # Asegúrate de que el campo en tu modelo se llame 'thread' o 'thread_id'
            return message_model.objects.create(thread_id=thread_id, sender=user, message=text)
        except Exception as e:
            print(f"Error guardando mensaje: {e}")
            return None