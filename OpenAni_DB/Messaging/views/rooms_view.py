from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Messaging.models import RoomModel, MessageModel
from Messaging.serializers import RoomSerializer

class RoomListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        threads = RoomModel.objects.filter(
            Q(user1=request.user) | Q(user2=request.user)
        ).order_by('-updated')

        serializer = RoomSerializer(threads, many=True, context={'request': request})
        return Response({"rooms": serializer.data})