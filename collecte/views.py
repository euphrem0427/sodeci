from django.shortcuts import render, redirect
from .models import *
from app.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from accounts.decorators import *
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


########################################################################
### Collecte de site functions
########################################################################

####Liste des collecte

@login_required(login_url='login')
def site_collect_list(request):
    collectes = CollectOnSite.objects.all()
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

# @login_required(login_url='login')
# def create_site_collect(request, id):
#     site = Site.objects.get(id=id)
    
#     site_collecte = SiteCollecte.objects.create(
#         site = site,
#         agent = request.user
#     )
#     url = '/add_site_collect/' + str(site_collecte.id) + '/'
#     return redirect(url)

# @login_required(login_url='login')
# def add_site_collect(request, id):
#     site = Site.objects.get(id=id)
    
#     settings = SettingSite.objects.all()
#     if request.POST:
#         site_collecte = SiteCollecte.objects.create(
#         site = site,
#         agent = request.user
#         )
#         for setting in settings:
#             value = request.POST[str(setting.id)]
#             try:
#                 is_exist = request.POST['is_exist'+str(setting.id)]
#                 is_exist = True
#             except MultiValueDictKeyError:
#                 is_exist = False
            
#             SiteCollecteDetail.objects.create(
#                 site_collecte = site_collecte,
#                 setting = setting,
#                 value = value,
#                 is_exist = is_exist
#                 )
            
#         return redirect('site_collect_list')

#     context={
#         'settings': settings
#     }
#     return render(request, 'pages/collecte/maintenance/add.html', context)

@login_required(login_url='login')
def add_collect_on_site(request, id):
    site = Site.objects.get(id=id)
    water = None
    water_form = WaterQualityForm()
    form = CollectOnSiteForm()
    if request.method == 'POST':
        form = CollectOnSiteForm(request.POST)
        if form.is_valid():
                collect = form.save(commit = False)
                collect.agent = request.user
                collect.site = site
                #collect.water_quality = water
                collect.save()
                return redirect('site_collect_list')
    context={'site':site}
    return render(request, 'pages/collecte/site/add.html', context)

@login_required(login_url='login')
def view_site_collect(request, id):
    collect = CollectOnSite.objects.get(id=id)
    #details = SiteCollecteDetail.objects.filter(site_collecte = collect, is_exist = True)
    context = {
        'collect': collect,
        #'details': details
    }
    return render(request, 'pages/collecte/site/view.html', context)


################################################################
### Parameters Functions
################################################################

@login_required(login_url='login')
def list_settings(request):
    settings = Setting.objects.all()
    context={'settings': settings}
    return render(request, 'pages/setting/maintenance/list.html', context)

@login_required(login_url='login')
def add_setting(request):
    form = SettingForm()
    if request.method == 'POST':
        form = SettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_setting')
    context={}
    return render(request, 'pages/setting/maintenance/add.html', context)


@login_required(login_url='login')
def view_setting(request, id):
    setting = Setting.objects.get(id=id)
    context = {'setting': setting}
    return render(request, 'pages/setting/maintenance/view.html', context)


@login_required(login_url='login')
def delete_setting(request, id):
    setting = Setting.objects.get(id=id)
    setting.delete()
    return redirect('list_setting')



@login_required(login_url='login')
def list_site_settings(request):
    settings = SettingSite.objects.all()
    context={'settings': settings}
    return render(request, 'pages/setting/site/list.html', context)

@login_required(login_url='login')
def add_site_setting(request):
    form = SettingSiteForm()
    if request.method == 'POST':
        form = SettingSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_site_setting')
    context={}
    return render(request, 'pages/setting/site/add.html', context)


@login_required(login_url='login')
def view_site_setting(request, id):
    setting = SettingSite.objects.get(id=id)
    context = {'setting': setting}
    return render(request, 'pages/setting/site/view.html', context)


@login_required(login_url='login')
def delete_site_setting(request, id):
    setting = SettingSite.objects.get(id=id)
    setting.delete()
    return redirect('list_setting')


################################################################
### Maintenance Functions
################################################################

@login_required(login_url='login')
def list_maintenance(request):
    maintenances = Maintenance.objects.all()
    context = {'maintenances':maintenances}
    return render(request,'pages/collecte/maintenance/list.html',context)

@login_required(login_url='login')
def choice_maintenance_site(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    return render(request,'pages/collecte/maintenance/choice_site.html',context)

@login_required(login_url='login')
def create_maintenance(request, id):
    site = Site.objects.get(id=id)
    
    maintenance = Maintenance.objects.create(
        site = site,
        agent = request.user
    )
    url = '/add_maintenance/' + str(maintenance.id) + '/'
    return redirect(url)

@login_required(login_url='login')
def add_maintenance(request, id):
    site = Site.objects.get(id=id)
    
    settings = Setting.objects.all()
    if request.POST:
        maintenance = Maintenance.objects.create(
        site = site,
        agent = request.user
    )
        for setting in settings:
            value = request.POST[str(setting.id)]
            try:
                is_exist = request.POST['is_exist'+str(setting.id)]
                is_exist = True
            except MultiValueDictKeyError:
                is_exist = False
            MaintenanceDetail.objects.create(
                maintenance = maintenance,
                setting = setting,
                value = value,
                is_exist = is_exist,
            )
        return redirect('list_maintenance')

    context={
        'settings': settings
    }
    return render(request, 'pages/collecte/maintenance/add.html', context)


@login_required(login_url='login')
def view_maintenance(request, id):
    maintenance = Maintenance.objects.get(id=id)
    details = MaintenanceDetail.objects.filter(maintenance = maintenance, is_exist = True)
    context = {
        'maintenance': maintenance,
        'details': details
    }
    return render(request, 'pages/collecte/maintenance/view.html', context)


@login_required(login_url='login')
def delete_maintenance(request, id):
    maintenance = Maintenance.objects.get(id=id)
    maintenance.delete()
    return redirect('list_maintenance')


@login_required(login_url='login')
def delete_site_collect(request, id):
    collect = CollectOnSite.objects.get(id=id)
    collect.delete()
    return redirect('site_collect_list')


################################################################
### Customer Collector
################################################################


@login_required(login_url='login')
def list_customer_collecte(request):
    customer_collectes = CustomerCollecte.objects.all()
    context = {'customer_collectes': customer_collectes}
    return render(request,'pages/collecte/customer/list.html',context)


@login_required(login_url='login')
def choice_customer(request):
    customers = Abonne.objects.all()
    context = {'customers': customers}
    return render(request,'pages/collecte/customer/choice.html',context)


@login_required(login_url='login')
def add_customer_collecte(request, id):
    customer = Abonne.objects.get(id=id)
    user = request.user

    form = CustomerCollecteForm()

    if request.method == 'POST':
        form = CustomerCollecteForm(request.POST, request.FILES)
        if form.is_valid():
            collect = form.save(commit = False)
            collect.user = user
            collect.abonne = customer
            collect.save()
            return redirect('list_customer_collecte')
        
    context = {}
    return render(request, 'pages/collecte/customer/add.html', context)


@login_required(login_url='login')
def delete_customer_collecte(request, id):
    collect = CustomerCollecte.objects.get(id=id)
    collect.delete()
    return redirect('list_customer_collecte')


@login_required(login_url='login')
def view_customer_collecte(request, id):
    collecte = CustomerCollecte.objects.get(id=id)
    context = {
        'collecte': collecte
    }
    return render(request, 'pages/collecte/customer/view.html', context)

