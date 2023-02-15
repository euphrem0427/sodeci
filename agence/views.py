from django.shortcuts import render, redirect
from app.models import *
from .forms import *
from .utils import *
# Create your views here.

def agence_list(request):
    agences = Agence.objects.all()
    context = {
        'agences': agences
    }
    return render(request, 'pages/agence/list.html', context)

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

def delete_agence(request, id):
    agence = Agence.objects.get(id=id)
    agence.delete()
    return redirect('agence_list')

def view_agence(request, id):
    agence = Agence.objects.get(id=id)
    context = {'agence': agence}
    return render(request, 'pages/agence/view.html', context)

################################################################
def site_list(request):
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'pages/site/list.html', context)

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

def delete_site(request, id):
    site = Site.objects.get(id=id)
    site.delete()
    return redirect('site_list')

def view_site(request, id):
    site = Site.objects.get(id=id)
    context = {'site': site}
    return render(request, 'pages/site/view.html', context)