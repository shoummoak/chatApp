from django.contrib import admin
# import models
from .models import User

# add the model to the admin panel UI
admin.site.register(User)

