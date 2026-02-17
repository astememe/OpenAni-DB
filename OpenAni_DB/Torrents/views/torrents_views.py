from rest_framework import permissions, status
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

    def get(self,request):
        torrents = TorrentModel.objects.all()
        serializer = TorrentSerializer(torrents, many=True)

        return Response(
            {
                "success": True,
                "data": data
            }, status=status.HTTP_200_OK
        )