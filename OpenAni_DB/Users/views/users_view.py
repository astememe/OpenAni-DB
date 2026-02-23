from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import UserModel
from Users.serializers import UserSerializer


class UserView(APIView):

    def get(self, request):
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)