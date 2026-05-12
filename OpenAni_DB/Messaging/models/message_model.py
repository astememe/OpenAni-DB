from django.db import models
from Messaging.models import RoomModel
from Users.models import UserModel

class MessageModel(models.Model):
    thread = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE,)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']