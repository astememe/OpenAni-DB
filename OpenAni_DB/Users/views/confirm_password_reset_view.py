import random

from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from Users.models import ResetPassword, UserModel


class ConfirmPasswordResetView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        reset_code = request.data.get('reset_code')

        reset_entry = ResetPassword.objects.filter(user__email=email, code=reset_code)

        if reset_entry:
            user = UserModel.objects.get(email=email)
            user.set_password(password)

