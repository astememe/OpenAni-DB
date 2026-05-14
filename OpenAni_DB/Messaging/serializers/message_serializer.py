from rest_framework import serializers
from Messaging.models import MessageModel

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = MessageModel
        fields = ['id', 'sender_username', 'text', 'timestamp']