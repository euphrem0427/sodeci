from django.shortcuts import render

# Create your views here.


def profil(request):
    return render(request, 'accounts/profil.html')

def login(request):
    return render(request, 'accounts/login.html')

def reset_password(request):
    return render(request, 'accounts/login.html')