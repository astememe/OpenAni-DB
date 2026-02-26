from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Torrents.models import ComentarioModel
from Users.models import UserModel, FavoritoModel
from Users.serializers import UserSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        nombre_viejo = user.username

        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            nombre_nuevo = user.username
            nueva_imagen = user.imagen

            ComentarioModel.objects.filter(nombre_usuario=nombre_viejo).update(
                nombre_usuario=nombre_nuevo,
                imagen_usuario=nueva_imagen,
            )

            FavoritoModel.objects.filter(nombre_usuario=nombre_viejo).update(
                nombre_usuario=nombre_nuevo,
            )

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def get(self, request):
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)