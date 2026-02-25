import random

from rest_framework import status
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
            user.save()
            reset_entry.delete()
            return Response({'message': "Contraseña cambiada con éxito"}, status=status.HTTP_201_CREATED)

        return Response({"Error": "Ha habido un error al cambiar la contraseña"}, status=status.HTTP_400_BAD_REQUEST)
