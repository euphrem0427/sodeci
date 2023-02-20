from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import *
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'pages/index.html')

def stats(request):
    return render(request, 'pages/stats/stat.html')