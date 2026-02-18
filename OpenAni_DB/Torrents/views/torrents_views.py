from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView

from ..serializers import TorrentSerializer
from ..models import TorrentModel


class TorrentViews(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        data = request.data
        serializer = TorrentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": True}, status=status.HTTP_201_CREATED)
        else:
            errores = []
            for error in serializer.errors.values():
                for e in error:
                    errores.append(e)

            return Response({"Errors": errores}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, torrent_nombre=None):
        nombre_query = request.query_params.get('nombre', None)
        id_query = request.query_params.get('id', None)

        if nombre_query and id_query:
            torrents = TorrentModel.objects.filter(nombre__icontains=nombre_query, id__icontains=id_query)
            serializer = TorrentSerializer(torrents, many=True)
            return Response({"torrents": serializer.data}, status=status.HTTP_200_OK)

        if nombre_query:
            torrents = TorrentModel.objects.filter(nombre__icontains=nombre_query)
            serializer = TorrentSerializer(torrents, many=True)
            return Response({"torrents": serializer.data}, status=status.HTTP_200_OK)

        if id_query:
            torrents = TorrentModel.objects.filter(id__icontains=id_query)
            serializer = TorrentSerializer(torrents, many=True)
            return Response({"torrents": serializer.data}, status=status.HTTP_200_OK)


        torrents = TorrentModel.objects.all()
        serializer = TorrentSerializer(torrents, many=True)
        return Response({"torrents": serializer.data}, status=status.HTTP_200_OK)