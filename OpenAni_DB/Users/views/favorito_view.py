from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Users.models import FavoritoModel
from Users.serializers import FavoritoSerializer


class FavoritoView(APIView):
    def get(self, request):
        favoritos = FavoritoModel.objects.filter(user=request.user)
        serializer = FavoritoSerializer(favoritos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        torrent_id = request.data.get('torrent_id')
        user = request.user

        favorito_qs = FavoritoModel.objects.filter(user=user, torrent_id=torrent_id)

        if not torrent_id:
            favorito_qs.delete()
            return Response(f"No se encontró torrent", status=status.HTTP_400_BAD_REQUEST)
        else:
            FavoritoModel.objects.create(user=user, torrent_id=torrent_id)
            return Response({"es_favorito": True}, status=status.HTTP_201_CREATED)