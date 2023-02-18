from django.shortcuts import render, redirect
from .models import *
from app.models import *
from .forms import *
# Create your views here.


########################################################################
### Collecte de site functions
########################################################################

####Liste des collecte

def site_collect_list(request):
    collectes = SiteCollecte.objects.all()
    context = {
        'collectes': collectes
    }
    return render(request, 'pages/collecte/site/list.html', context)

def choice_site_collect(request):
    
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'pages/collecte/site/choice_site.html', context)

def add_site_collect(request, id):
    site = Site.objects.get(id=id)
    form = SiteCollecteForm()
    if request.method == "POST":
        form =SiteCollecteForm(request.POST)
        if form.is_valid():
            collect = form.save(commit = False)
            collect.site = site
            collect.agent = request.user
            collect.save()
            return redirect('site_collect_list')
    context = {
        'site': site,
    }
    return render(request, 'pages/collecte/site/add.html', context)

def view_site_collect(request, id):
    collect = SiteCollecte.objects.get(id=id)
    context = {
        'collect': collect
    }
    return render(request, 'pages/collecte/site/view.html', context)