from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Torrents.models import ComentarioModel
from Torrents.serializers.comentario_serializer import ComentarioSerializer


class ComentarioView(APIView):
    def get(self, request):
        nombre_torrent_query = request.query_params.get('nombre_torrent', None)
        nombre_usuario_query = request.query_params.get('nombre_user', None)
        if nombre_usuario_query:
            comentarios = ComentarioModel.objects.filter(nombre_usuario__icontains=nombre_torrent_query)
            serializer = ComentarioSerializer(comentarios, many=True)
            return Response({"comentarios": serializer.data}, status=status.HTTP_200_OK)
        if nombre_torrent_query:
            favoritos = ComentarioModel.objects.filter(nombre_torrent__icontains=nombre_torrent_query)
            serializer = ComentarioSerializer(favoritos, many=True)
            return Response({"comentarios": serializer.data}, status=status.HTTP_200_OK)
        comentarios = ComentarioModel.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ComentarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": True}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)