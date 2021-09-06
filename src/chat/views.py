# imports
from django.shortcuts import render

from accounts.models import User
from .models import *

# views

# def index(request):
#     return render(request, 'chat/index.html')

def room(request, user, room_name):

    # grab the other user (NOT self)
    socket = Socket.objects.filter(socket=room_name)[0]
    if socket.user1.username == user:
        user2 = socket.user2.username
    else:
        user2 = socket.user1.username

    # the following are passed onto the html frontend 
    # websocket/room_name 
    # account username
    # message_list which contains messages of entire conversation in the given websocket
    context = {
        'room_name' : room_name,
        'user' : User.objects.filter(username=user)[0],
        'user2' : User.objects.filter(username=user2)[0],
        'message_list' : Message.objects.filter(socket=socket),
    }

    return render(request, 'chat/room2.html', context)
