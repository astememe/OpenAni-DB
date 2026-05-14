from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from Messaging.models import MessageModel, RoomModel
from Messaging.serializers import MessageSerializer


class MessageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        room_id = request.query_params.get('room_id')

        room = RoomModel.objects.filter(
            Q(id=room_id) & (Q(user1=request.user) | Q(user2=request.user))
        ).first()

        if not room:
            return Response({"error": "No tienes permiso o la sala no existe"}, status=status.HTTP_403_FORBIDDEN)

        messages = MessageModel.objects.filter(room=room)
        serializer = MessageSerializer(messages, many=True)

        return Response({"messages": serializer.data})