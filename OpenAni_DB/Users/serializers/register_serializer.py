from rest_framework import serializers

from Users.models import UserModel


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    imagen = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ("username", "email", "imagen",
                  "password", "confirm_password")

    def validate_email(self, value):
        user = UserModel.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email already registered")
        return value

    def validate_password(self, value):
        tiene_numero = any(letra.isdigit() for letra in value)
        if not tiene_numero:
            raise serializers.ValidationError("Password must contain at least one number")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")

        user = UserModel.objects.create_user(
            password = password,
            **validated_data
        )
        return user