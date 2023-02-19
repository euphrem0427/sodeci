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
@allowed_users(allowed_roles=['manager'])
def agence_list(request):
    agences = Agence.objects.all()
    context = {
        'agences': agences
    }
    return render(request, 'pages/agence/list.html', context)

### ADDING AGENCE ###

def add_agence(request):
    form = AgenceForm()
    if request.method == 'POST':
        form = AgenceForm(request.POST)
        if form.is_valid():
            agence = form.save(commit=False)
            agence.code = agence_code()
            agence.save()
            return redirect('agence_list')
    context = {}
    return render(request, 'pages/agence/add.html', context)

### EDITING AGENCE ###

def edit_agence(request, id):
    agence = Agence.objects.get(id=id)
    form = AgenceForm(
        instance=agence, 
        initial = {
            'title':agence.title,
            'description':agence.description,
            'adresse':agence.adresse,
            'phone':agence.phone,
            'email':agence.email
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
            'email':agence.email
            })
        if form.is_valid():
            form.save()
            return redirect("agence_list")
    context = {'agence': agence}
    return render(request, 'pages/agence/edit.html', context)

### DELETE AGENCE ###

def delete_agence(request, id):
    agence = Agence.objects.get(id=id)
    agence.delete()
    return redirect('agence_list')


#### View Details Agence ###

def view_agence(request, id):
    agence = Agence.objects.get(id=id)
    context = {'agence': agence}
    return render(request, 'pages/agence/view.html', context)

################################################################
###Site Management
################################################################

### Site LISTE ###

def site_list(request):
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'pages/site/list.html', context)

### ADDING SITE ###

def add_site(request):
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
    }
    return render(request, 'pages/site/add.html', context)

### EDITING SITE ###

def edit_site(request, id):
    agences = Agence.objects.all()
    site = Site.objects.get(id=id)
    form = SiteForm(
        instance=site, 
        initial = {
            'title':site.title,
            'description':site.description,
            'adresse':site.adresse,
            'agence':site.agence,
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
            })
        if form.is_valid():
            form.save()
            return redirect("site_list")
    context = {
        'agences': agences,
        'site': site,
        }
    return render(request, 'pages/site/edit.html', context)

### DELETE SITE ###

def delete_site(request, id):
    site = Site.objects.get(id=id)
    site.delete()
    return redirect('site_list')

### VIEW SITE ###

def view_site(request, id):
    site = Site.objects.get(id=id)
    context = {'site': site}
    return render(request, 'pages/site/view.html', context)

########################################################################
###Nos abonnées
########################################################################

### LISTING CUSTOMERS ###

def list_abonne(request):
    abonnes = Abonne.objects.all()
    context = {
        'abonnes': abonnes
    }
    return render(request, 'pages/abonne/list.html', context)

### ADDING CUSTOMERS ###

def add_abonne(request):
    agences = Agence.objects.all()
    form = AbonneForm()
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_abonne')
    context = {
        'agences': agences,
    }
    return render(request, 'pages/abonne/add.html', context)

### EDITING CUSTOMERS ###

def edit_abonne(request, id):

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
            })
        if form.is_valid():
            form.save()
            return redirect("list_abonne")
    context = {
        'abonne': abonne,
        'agences':agences
    }
    return render(request, 'pages/abonne/edit.html', context)

### VIEWING CUSTOMERS ###

def view_abonne(request, id):
    abonne = Abonne.objects.get(id=id)
    context = {
        'abonne': abonne
    }
    return render(request, 'pages/abonne/view.html', context)

### DELETING CUSTOMERS ###

def delete_abonne(request, id):
    abonne = Abonne.objects.get(id=id)
    abonne.delete()
    return redirect('list_abonne')

### IMPORTING ABONNE ###

def import_abonne(request):
    context = {}
    return render(request, 'pages/abonne/import.html', context)

### Export ABONNE ###

def export_abonne(request):
    context = {}
    return render(request, 'pages/abonne/export.html', context)
