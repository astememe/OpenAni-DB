from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Users.models import FavoritoModel
from Users.serializers import FavoritoSerializer


class FavoritoView(APIView):
    def get(self, request):
        favoritos = FavoritoModel.objects.all()
        serializer = FavoritoSerializer(favoritos, many=True)
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