# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *



class ChatConsumer(WebsocketConsumer):

    """ BACKEND LOGIC METHODS """
    # methods that perform logical tasks

    # save message to db
    def save_message(self, sender_user, message):
        # get the room name
        room_name = self.scope['url_route']['kwargs']['room_name']
        # get Socket obj from room_name
        active_socket_obj = Socket.objects.filter(socket=room_name)[0]
        receiver_user = ChatConsumer.get_receiver_user(sender_user, active_socket_obj)
        # Message consists of the socket_obj, actual message, and sender-receiver user pair
        message_obj = Message(socket=active_socket_obj, content=message, sender_user=sender_user, receiver_user=receiver_user)
        message_obj.save()


    # figure out who seld.user is chatting with in the websocket
    def get_receiver_user(sender, socket):

        if socket.user1.username == sender:
            return socket.user2.username
        else:
            return socket.user1.username


    """ WEBSOCKET METHODS """
    # The ones communicating with the websocket  
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket. Check the js line in room.html --> chatSocket.send(JSON.stringify({'message': message}));
    def receive(self, text_data):
        # load the json
        text_data_json = json.loads(text_data)
        # parse message from JSON
        message = text_data_json['message']
        username = text_data_json['user']

        # Send message to room group
        # this allows for the chat_message method to access and send the message back to the websocket
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user' : username,
            }
        )
        # take message and store in db. Note that the message instance's sender and receiver information are disambiguated
        self.save_message(username, message)

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket. This message gets dumped onto chatSocket.onmessage() in the room.html js script
        self.send(text_data=json.dumps({
            'message': message,
            'user' : user
        }))
