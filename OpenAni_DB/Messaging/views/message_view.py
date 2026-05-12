from rest_framework.views import APIView
from rest_framework.response import Response
from Messaging.models import MessageModel, RoomModel
from Messaging.serializers import MessageSerializer

class MessageListView(APIView):
    def get(self, request):
        thread_id = request.query_params.get('group_id')
        messages = MessageModel.objects.filter(thread_id=thread_id)
        serializer = MessageSerializer(messages, many=True)

        return Response({"messages": serializer.data})