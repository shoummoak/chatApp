from django.db import models
from django.db.models.fields import DateTimeField
from accounts.models import User

class Message(models.Model):

    # attributes
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_receiver')
    content = models.CharField(max_length=500)
    datetime = DateTimeField('message datetime', auto_now_add=True)     # timestamp of message automatically added when message is created


class Notification(models.Model):

    # attributes
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='not_sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='not_receiver')
    datetime = DateTimeField('notification datetime')

