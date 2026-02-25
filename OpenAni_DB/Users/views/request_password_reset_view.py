import random

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import ResetPassword, UserModel


class RequestPasswordResetView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data['email']
        user = UserModel.objects.filter(email=email).first()

        if user:
            code = str(random.randint(100000, 999999))
            ResetPassword.objects.create(user=user, code=code)
            return Response({'code': code, 'email': email}, status=status.HTTP_201_CREATED)

        return Response({'error': "No se encuentra el usuario."}, status=status.HTTP_404_NOT_FOUND)