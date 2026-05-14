from rest_framework import serializers
from Messaging.models import RoomModel
from Users.models import UserModel

class RoomCreateSerializer(serializers.ModelSerializer):
    other_user_username = serializers.CharField(write_only=True)

    class Meta:
        model = RoomModel
        fields = ['id', 'other_user_username']

    def validate_other_user_username(self, value):
        if not UserModel.objects.filter(username=value).exists():
            raise serializers.ValidationError("El usuario no existe.")
        return value