from django.shortcuts import render, redirect
from .models import *
from app.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from accounts.decorators import *
# Create your views here.


########################################################################
### Collecte de site functions
########################################################################

####Liste des collecte

@login_required(login_url='login')
def site_collect_list(request):
    collectes = SiteCollecte.objects.all()
    context = {
        'collectes': collectes
    }
    return render(request, 'pages/collecte/site/list.html', context)

@login_required(login_url='login')
def choice_site_collect(request):
    
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'pages/collecte/site/choice_site.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def view_site_collect(request, id):
    collect = SiteCollecte.objects.get(id=id)
    context = {
        'collect': collect
    }
    return render(request, 'pages/collecte/site/view.html', context)


################################################################
### Parameters Functions
################################################################

@login_required(login_url='login')
def list_settings(request):
    settings = Setting.objects.all()
    context={'settings': settings}
    return render(request, 'pages/setting/list.html', context)

@login_required(login_url='login')
def add_setting(request):
    form = SettingForm()
    if request.method == 'POST':
        form = SettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_setting')
    context={}
    return render(request, 'pages/setting/add.html', context)


@login_required(login_url='login')
def view_setting(request, id):
    setting = Setting.objects.get(id=id)
    context = {'setting': setting}
    return render(request, 'pages/setting/view.html', context)


@login_required(login_url='login')
def delete_setting(request, id):
    setting = Setting.objects.get(id=id)
    setting.delete()
    return redirect('list_setting')