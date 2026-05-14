from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Messaging.models import RoomModel, MessageModel
from Messaging.serializers import RoomSerializer
from Messaging.serializers.room_create_serializer import RoomCreateSerializer
from Users.models import UserModel


class RoomListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        threads = RoomModel.objects.filter(
            Q(user1=request.user) | Q(user2=request.user)
        ).order_by('-updated')

        serializer = RoomSerializer(threads, many=True, context={'request': request})
        return Response({"rooms": serializer.data})

    def post(self, request):
        serializer = RoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            other_user = UserModel.objects.get(username=serializer.validated_data['other_user_username'])
            user1 = request.user
            user2 = other_user

            if user1 == user2:
                return Response({"error": "No puedes crear un chat contigo mismo"}, status=status.HTTP_400_BAD_REQUEST)

            room = RoomModel.objects.filter(
                (Q(user1=user1) & Q(user2=user2)) | (Q(user1=user2) & Q(user2=user1))
            ).first()

            if not room:
                room = RoomModel.objects.create(user1=user1, user2=user2)
                status_code = status.HTTP_201_CREATED
            else:
                status_code = status.HTTP_200_OK

            return Response(
                RoomSerializer(room, context={'request': request}).data,
                status=status_code
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)