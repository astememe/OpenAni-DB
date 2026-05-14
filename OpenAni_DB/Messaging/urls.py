from django.urls import path
from Messaging.views import MessageListView, RoomListView

urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='room_list'),

    path('messages/', MessageListView.as_view(), name='message_list'),
]