
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import UserForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_username = form.cleaned_data['user_username']
            user_password = form.cleaned_data['user_password']
            
            # check if data is being received
            print(user_name)
            print(user_email)
            print(user_username)
            print(user_password)
            # save new user in db
            new_user = User(name=user_name, email=user_email, username=user_username, password=user_password)
            new_user.save()


    form = UserForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def dummy(request):
    return render(request, 'accounts/dummy.html')



