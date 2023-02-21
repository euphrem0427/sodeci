from django.forms import *
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "email", "site", "agence")

class SetPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "phone", "password1", "password2")

class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ("name",)