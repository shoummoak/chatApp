from django.test.utils import setup_test_environment
from django.test import TestCase, Client
from django.urls import reverse
from .models import User

from chat.models import Socket, Message
from chat.views import *


# testing the User model
class UserModelTestCase(TestCase):
    
    # test if software prevents similar usernames
    def test_prevent_duplicate_username(self):
        try:
            User.objects.create(name="asdasd", email="qweqwe@test.com", username="test_username", password="qweqwe")
            User.objects.create(name="qweqwe", email="asdasd@test.com", username="test_username", password="asdasd")
        except:
            print("User could not be created")
        self.assertIs(User.objects.filter(username="test_username").count() > 1, False)

    # test if software prevents similar usernames
    def test_prevent_duplicate_email(self):
        try:
            User.objects.create(name="asdasd", email="test@test.com", username="asdasd", password="qweqwe")
            User.objects.create(name="qweqwe", email="test@test.com", username="qweqwe", password="asdasd")
        except:
            print("User could not be created")
        self.assertIs(User.objects.filter(email="test@test.com").count() > 1, False)


# testing the Accounts views
class AccountsViewTest(TestCase):

    def setup(self):
        setup_test_environment()
        self.client = Client()
    
    def test_registration(self):
        response = self.client.get(reverse('register'))
        # test whether the client is receiving the page
        self.assertEquals(response.status_code, 200)
        

    def test_login(self):
        response = self.client.get(reverse('login'))
        # test whether the client is receiving the page
        self.assertEquals(response.status_code, 200)

class ChatModelsTest(TestCase):

    def test_save_messages(self):
        message_saved = save_message(message="checking new message", sender="user1", receiver="user2")
        self.assertIs(message_saved, True)

    def test_send_messages(self):
        message_sent = send_message(message="checking new message")
        self.assertIs(message_sent, True)

    def test_receive_messages(self):
        message_received = receive_message(message="checking new message")
        self.assertIs(message_received, True)

    def test_connect_socket(self):
        connection = connect()
        self.assertIs(connection, True)

    def test_disconnect_socket(self):
        connection = disconnect()
        self.assertIs(connection, True)
