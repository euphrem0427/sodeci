from django.shortcuts import render, redirect
from app.models import *
from .forms import *
from .utils import *
from django.contrib.auth.decorators import login_required
from accounts.decorators import *
# Create your views here.


########################################################################
### Agence functions ###
########################################################################

### Agence list ###

@login_required(login_url='login')
def agence_list(request):
    agences = Agence.objects.all()
    context = {
        'agences': agences
    }
    return render(request, 'pages/agence/list.html', context)

### ADDING AGENCE ###

@login_required(login_url='login')
def add_agence(request):
    departements = Departement.objects.all()
    form = AgenceForm()
    if request.method == 'POST':
        form = AgenceForm(request.POST)
        if form.is_valid():
            agence = form.save(commit=False)
            agence.code = agence_code()
            agence.save()
            return redirect('agence_list')
    context = {
        'departements':departements
    }
    return render(request, 'pages/agence/add.html', context)

### EDITING AGENCE ###

@login_required(login_url='login')
def edit_agence(request, id):
    departements = Departement.objects.all()
    agence = Agence.objects.get(id=id)
    form = AgenceForm(
        instance=agence, 
        initial = {
            'title':agence.title,
            'description':agence.description,
            'adresse':agence.adresse,
            'phone':agence.phone,
            'email':agence.email,
            'departement':agence.departement,
            })
    if request.method == "POST":
        form = AgenceForm(
            request.POST,
            instance=agence, 
            initial = {
            'title':agence.title,
            'description':agence.description,
            'adresse':agence.adresse,
            'phone':agence.phone,
            'email':agence.email,
            'departement':agence.departement,
            })
        if form.is_valid():
            form.save()
            return redirect("agence_list")
    context = {'agence': agence, 'departements':departements}
    return render(request, 'pages/agence/edit.html', context)

### DELETE AGENCE ###

@login_required(login_url='login')
def delete_agence(request, id):
    agence = Agence.objects.get(id=id)
    agence.delete()
    return redirect('agence_list')


#### View Details Agence ###

@login_required(login_url='login')
def view_agence(request, id):
    agence = Agence.objects.get(id=id)
    context = {'agence': agence}
    return render(request, 'pages/agence/view.html', context)

################################################################
###Site Management
################################################################

### Site LISTE ###

@login_required(login_url='login')
def site_list(request):
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'pages/site/list.html', context)

### ADDING SITE ###

@login_required(login_url='login')
def add_site(request):
    departements = Departement.objects.all()
    communes = Commune.objects.all()
    agences = Agence.objects.all()
    form = SiteForm()
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.code = site_code()
            site.save()
            return redirect('site_list')
    context = {
        'agences': agences,
        'departements':departements,
        'communes':communes,
    }
    return render(request, 'pages/site/add.html', context)

### EDITING SITE ###

@login_required(login_url='login')
def edit_site(request, id):
    departements = Departement.objects.all()
    communes = Commune.objects.all()
    agences = Agence.objects.all()
    site = Site.objects.get(id=id)
    form = SiteForm(
        instance=site, 
        initial = {
            'title':site.title,
            'description':site.description,
            'adresse':site.adresse,
            'agence':site.agence,
            'departement':site.departement,
            'commune':site.commune,
            })
    if request.method == "POST":
        form = SiteForm(
            request.POST,
            instance=site, 
            initial = {
            'title':site.title,
            'description':site.description,
            'adresse':site.adresse,
            'agence':site.agence,
            'departement':site.departement,
            'commune':site.commune,
            })
        if form.is_valid():
            form.save()
            return redirect("site_list")
    context = {
        'agences': agences,
        'site': site,
        'communes':communes,
        'departements':departements,
        }
    return render(request, 'pages/site/edit.html', context)

### DELETE SITE ###

@login_required(login_url='login')
def delete_site(request, id):
    site = Site.objects.get(id=id)
    site.delete()
    return redirect('site_list')

### VIEW SITE ###

@login_required(login_url='login')
def view_site(request, id):
    site = Site.objects.get(id=id)
    context = {'site': site}
    return render(request, 'pages/site/view.html', context)

########################################################################
###Nos abonnées
########################################################################

### LISTING CUSTOMERS ###

@login_required(login_url='login')
def list_abonne(request):
    abonnes = Abonne.objects.all()
    context = {
        'abonnes': abonnes
    }
    return render(request, 'pages/abonne/list.html', context)

### ADDING CUSTOMERS ###

@login_required(login_url='login')
def add_abonne(request):
    departements = Departement.objects.all()
    communes = Commune.objects.all()
    agences = Agence.objects.all()
    form = AbonneForm()
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_abonne')
    context = {
        'agences': agences,
        'communes':communes,
        'departements':departements,
    }
    return render(request, 'pages/abonne/add.html', context)

### EDITING CUSTOMERS ###

@login_required(login_url='login')
def edit_abonne(request, id):
    departements = Departement.objects.all()
    communes = Commune.objects.all()
    abonne = Abonne.objects.get(id=id)
    agences = Agence.objects.all()
    form = AbonneForm(
        instance=abonne, 
        initial = {
            'first_name':abonne.first_name,
            'last_name':abonne.last_name,
            'adresse':abonne.adresse,
            'agence':abonne.agence,
            'phone':abonne.phone,
            'ifu':abonne.ifu,
            'departement':abonne.departement,
            'commune':abonne.commune,
            })
    if request.method == "POST":
        form = AbonneForm(
            request.POST,
            instance=abonne, 
            initial = {
            'first_name':abonne.first_name,
            'last_name':abonne.last_name,
            'adresse':abonne.adresse,
            'agence':abonne.agence,
            'phone':abonne.phone,
            'ifu':abonne.ifu,
            'departement':abonne.departement,
            'commune':abonne.commune,
            })
        if form.is_valid():
            form.save()
            return redirect("list_abonne")
    context = {
        'abonne': abonne,
        'agences':agences,
        'communes':communes,
        'departements':departements,
    }
    return render(request, 'pages/abonne/edit.html', context)

### VIEWING CUSTOMERS ###

@login_required(login_url='login')
def view_abonne(request, id):
    abonne = Abonne.objects.get(id=id)
    context = {
        'abonne': abonne
    }
    return render(request, 'pages/abonne/view.html', context)

### DELETING CUSTOMERS ###

@login_required(login_url='login')
def delete_abonne(request, id):
    abonne = Abonne.objects.get(id=id)
    abonne.delete()
    return redirect('list_abonne')

### IMPORTING ABONNE ###

@login_required(login_url='login')
def import_abonne(request):
    context = {}
    return render(request, 'pages/abonne/import.html', context)

### Export ABONNE ###

@login_required(login_url='login')
def export_abonne(request):
    context = {}
    return render(request, 'pages/abonne/export.html', context)


################################################################
## Département & Commune
################################################################    

def list_departement(request):
    departements = Departement.objects.all()
    context = {
        'departements': departements
    }
    return render(request, 'pages/setting/departement/list.html', context)

def add_departement(request):
    form = DepartementForm()
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_departement')
        
    return render(request, 'pages/setting/departement/add.html')

def view_departement(request, id):
    departement = Departement.objects.get(id=id)
    context = {
        'departement': departement
    }
    return render(request, 'pages/setting/departement/view.html', context)


def delete_departement(request, id):
    departement = Departement.objects.get(id=id)
    departement.delete()
    return redirect('list_departement')



def list_commune(request):
    communes = Commune.objects.all()
    context = {
        'communes': communes
    }
    return render(request, 'pages/setting/commune/list.html', context)

def add_commune(request):
    departements = Departement.objects.all()
    form = CommuneForm()
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commune')
    context = {'departements': departements}
    return render(request, 'pages/setting/commune/add.html', context)

def view_commune(request, id):
    commune = Commune.objects.get(id=id)
    context = {
        'commune': commune
    }
    return render(request, 'pages/setting/commune/view.html', context)

def delete_commune(request, id):
    commune = Commune.objects.get(id=id)
    commune.delete()
    return redirect('list_commune')