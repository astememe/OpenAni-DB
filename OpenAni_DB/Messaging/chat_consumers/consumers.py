import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from Messaging.models import MessageModel, RoomModel # Nombres correctos
from Users.models import UserModel

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.room_group_name = f'chat_{self.group_id}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data.get('message')
        username = data.get('sender_username')

        msg_obj = await self.save_message(username, self.group_id, message_text)

        if msg_obj:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': msg_obj.text,
                    'sender_username': msg_obj.sender.username,
                    'timestamp': msg_obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self, username, room_id, text):
        try:
            user = UserModel.objects.get(username=username)
            room = RoomModel.objects.get(id=room_id)
            return MessageModel.objects.create(room=room, sender=user, text=text)
        except Exception as e:
            print(f"Error guardando mensaje: {e}")
            return None