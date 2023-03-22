from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import *
from accounts.models import *
from collecte.models import *
from agence.models import *
from .models import *
# Create your views here.

@login_required(login_url='login')
def home(request):
    users = User.objects.all().count()
    abonnes = Abonne.objects.all().count()
    collecte_abonnes = CustomerCollecte.objects.all().count()
    collecte_sites = SiteCollecte.objects.all().count()
    maintenances = Maintenance.objects.all().count()
    agences = Agence.objects.all().count()

    context = {
        "users": users,
        "abonnes": abonnes,
        "collecte_abonnes": collecte_abonnes,
        "collecte_sites": collecte_sites,
        "maintenances": maintenances,
        'agences': agences,
    }
    return render(request, 'pages/index.html', context)

def stats(request):
    return render(request, 'pages/stats/stat.html')