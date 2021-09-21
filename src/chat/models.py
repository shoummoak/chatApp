from django.db import models
from django.db.models.fields import DateTimeField
from accounts.models import User


# Socket is unique for any pair of users commincating in the same websocket
# Note that Socket obj essentially has two user obj as its attributes instead of just the users' pk
class Socket(models.Model):

    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='party1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='party2')
    socket = models.IntegerField(default=0)

    def __str__(self):
        return "{} | {} | {}".format(self.user1, self.user2, self.socket)


# contains messages occured in a particular websocket comprising of two users
class Message(models.Model):

    socket = models.ForeignKey(Socket, on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=500, default="dummy")
    sender_user = models.CharField(max_length=500, default="dummy")
    receiver_user = models.CharField(max_length=500, default="dummy")
    # datetime = DateTimeField('message datetime', auto_now_add=True)     # timestamp of message automatically added when message is created


