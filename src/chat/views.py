# imports

from django.shortcuts import render

# views

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    nile = 'Nile'
    return render(request, 'chat/room2.html', {
        'room_name' : room_name,
    })
