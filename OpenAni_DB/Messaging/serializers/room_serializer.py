from rest_framework import serializers
from Messaging.models import RoomModel, MessageModel

class RoomSerializer(serializers.ModelSerializer):
    other_user = serializers.SerializerMethodField()
    other_user_img = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()
    last_message_timestamp = serializers.SerializerMethodField()

    class Meta:
        model = RoomModel
        fields = ['id', 'other_user', 'other_user_img', 'last_message', 'last_message_timestamp']

    def get_other_user(self, obj):
        request_user = self.context.get('request').user
        return obj.user2.username if obj.user1 == request_user else obj.user1.username

    def get_last_message(self, obj):
        last = obj.messages.last()
        return last.text if last else "No hay mensajes aún"

    def get_last_message_timestamp(self, obj):
        last = obj.messages.last()
        return last.timestamp if last else None

    def get_other_user_img(self, obj):
        request_user = self.context.get('request').user
        return obj.user2.imagen if obj.user1 == request_user else obj.user1.imagen
