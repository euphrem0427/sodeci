from django.forms import *
from .models import User
from app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class UserForm(ModelForm):
    groups = ModelChoiceField(queryset=Group.objects.all(), required=True)
    site = ModelChoiceField(queryset=Site.objects.all(), required=True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "email", "site", "agence", "groups")

class SetPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "phone", "password1", "password2")

class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ("name",)


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "email")

class UpgradeUserForm(ModelForm):
    groups = ModelChoiceField(queryset=Group.objects.all(), required=True)
    site = ModelChoiceField(queryset=Site.objects.all(), required=True)
    class Meta:
        model = User
        fields = ("site", "agence", "groups")