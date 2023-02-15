from django.shortcuts import render
from .models import User

# Create your views here.

def profil(request):
    return render(request, 'accounts/profil.html')

def login(request):
    return render(request, 'accounts/login.html')

def reset_password(request):
    return render(request, 'accounts/login.html')

def list_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'pages/users/list.html', context)

def add_user(request):
    context ={}
    return render(request, 'pages/users/add.html', context)

def edit_user(request):
    context ={}
    return render(request, 'pages/users/edit.html', context)

def upgrade_user(request):
    context ={}
    return render(request, 'pages/users/upgrade.html', context)

def delete_user(request):
    context ={}
    return render(request, 'pages/users/delete.html', context)

def view_user(request):
    context ={}
    return render(request, 'pages/users/view.html', context)

