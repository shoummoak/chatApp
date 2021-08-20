
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# import forms
from .forms import UserForm

def register(request):

    # if the form submit button has been clicked, a POST method has been called
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():     
            # check if data is being received
            # print(form.cleaned_data['username'])
            # create a user with the form data, and save in the User database
            form.save()

    # in case the webpage was simply loaded, a GET method has been called
    # pass the blank form into register.html where it will be rendered
    form = UserForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def dummy(request):
    return render(request, 'accounts/dummy.html')



