from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(label='First Name', max_length=100)
    user_email = forms.CharField(label='Email', max_length=100)
    user_username = forms.CharField(label='Username', max_length=100)
    user_password = forms.CharField(label='Password', max_length=100)