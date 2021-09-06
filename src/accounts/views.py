
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import User


# function to check login credentials with database
def authenticate_login(username_or_email, password):
    if (User.objects.filter(username=username_or_email) or User.objects.filter(email=username_or_email)) and User.objects.filter(password=password):
        return True
    else:
        return False


# import forms
from .forms import UserForm, LoginForm

def register(request):

    # if the form submit button has been clicked, a POST method has been called
    if request.method == 'POST':
        form = UserForm(request.POST)
        print('POST sent')
        if form.is_valid():
            print('valid form')
            # check if data is being received
            # print(form.cleaned_data['username'])
            # create a user with the form data, and save in the User database
            saved_form = form.save()
            print(saved_form)
            # return redirect('login/')
            return redirect('http://127.0.0.1:8000/login/')

    print('GET requested')
    # in case the webpage was simply loaded, a GET method has been called
    # pass the blank form into register.html where it will be rendered
    form = UserForm()
    context = {'form':form}
    return render(request, 'accounts/register2.html', context)

# if login request as GET, generate the html with an empty form for user to fill up
# if login request as POST, validate credentials, and redirect to user's chat dashboard
def login(request):

    # if the form submit button has been clicked, a POST method has been called
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('valid form')
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            # check if backend is receiving data
            print('username: {}\npass: {}'.format(username_or_email, password))
            if authenticate_login(username_or_email, password):
                print('Login Successful')
                return redirect('http://127.0.0.1:8000/user/{}/1'.format(username_or_email))
            else:
                print('Login Failed')
            return redirect('http://127.0.0.1:8000/login/')

    # if the request is a simple GET request
    form = LoginForm()
    context = {'form': form}
    return render(request, 'accounts/login2.html', context)

# dummy routing
def dummy(request):
    return render(request, 'accounts/dummy.html')

