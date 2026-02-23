import random

from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from Users.models import ResetPassword

class ConfirmPasswordResetView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data['email']
        user = User.objects.filter(email=email).first()

        if user:
            code = str(random.randint(100000, 999999))
            ResetPassword.objects.create(user=user, code=code)