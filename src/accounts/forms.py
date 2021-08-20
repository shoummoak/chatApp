from django.forms import ModelForm
from .models import User

# create a form with input fields which correspond to the User database fields
class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'