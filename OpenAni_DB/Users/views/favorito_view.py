from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from Users.models import FavoritoModel
from Users.serializers import FavoritoSerializer


class FavoritoView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        favoritos = FavoritoModel.objects.all()
        nombre_user_query = request.query_params.get('nombre_usuario', None)
        serializer = FavoritoSerializer(favoritos, many=True)
        if nombre_user_query:
            favoritos = FavoritoModel.objects.filter(nombre_usuario__icontains=nombre_user_query)
            serializer = FavoritoSerializer(favoritos, many=True)
            return Response({"favoritos": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = FavoritoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": True}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)