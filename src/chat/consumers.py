# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):

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

        # Send message to room group
        # this allows for the chat_message method to access and send the message back to the websocket
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user' : 'Nile'
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket. This message gets dumped onto chatSocket.onmessage() in the room.html js script
        self.send(text_data=json.dumps({
            'message': message,
            'user' : user
        }))