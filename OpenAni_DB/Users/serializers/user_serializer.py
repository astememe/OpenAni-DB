from rest_framework import serializers

from Users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'imagen', 'descripcion']
        extra_kwargs = {'password': {'write_only': True, 'required': False, 'allow_blank': True},
                        'username': {'required': False},
                        'email': {'required': False}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password and password != "":
            instance.set_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance