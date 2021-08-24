from django import forms
from .models import User

# simple registration form
# create a form with input fields which correspond to the User database fields
class UserForm(forms.ModelForm):
    
    class Meta:

        model = User
        # these are the fields of the actual User model 
        fields = ['name', 'email', 'username', 'password']
        # widgets to tag classes and such to the individual form fields in the html
        widgets = {
            'name' : forms.TextInput(attrs={'class':'input100', 'placeholder':'Display Name'}),
            'email' : forms.EmailInput(attrs={'class':'input100', 'placeholder':'Email'}),
            'username' : forms.TextInput(attrs={'class':'input100', 'placeholder':'Username'}),
            'password' : forms.PasswordInput(attrs={'class':'input100', 'placeholder':'Password'}),
        }


# simple login form
class LoginForm(forms.Form):

    # customize the fields with widgets just like the UserForm
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={'class':'input100', 'placeholder':'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder':'Password'}))
    
