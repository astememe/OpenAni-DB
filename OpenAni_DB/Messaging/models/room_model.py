from django.db import models
from Users.models import UserModel

class RoomModel(models.Model):
    user1 = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='thread_user1')
    user2 = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='thread_user2')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user1', 'user2']