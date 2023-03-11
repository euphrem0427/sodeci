from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login as login_auth, logout as logout_auth, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import *
from .utils import *
from .forms import *
from django.core.mail import send_mail
from sodeci.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail, BadHeaderError
from app.models import *
from django.contrib.auth.models import Group
from django.db.models import Q
# Create your views here.

@login_required(login_url='login')
def profil(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'accounts/profil.html', context)

@unauthentificated_user
def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('home')
        else:
            message = "Identifiant incorrect"
    context={}
    return render(request, 'accounts/login.html', context)

def logout(request):
    logout_auth(request)
    return redirect('login')

def reset_password(request):
    if request.POST:
        username = request.POST['username']
        try:
            user = User.objects.get(Q(email=username) | Q(phone=username))
        except User.DoesNotExist:
            return None
        else:
            email = user.email
            subject = "Modifiacation de mot de passe"
            email_template_name = "partials/mails/user_creation.html"
            ctxt = {
                "name": user.first_name,
                "link": "http://127.0.0.1:8000/accounts/set_password/" + str(user.username) + "/"
            }
            html_message = render_to_string(email_template_name, ctxt)
            plain_message = strip_tags(html_message)
            mail = EmailMultiAlternatives(
                subject,
                plain_message,
                'OMILAYE <euphrem0427@gmail.com>' ,
                [email]
            )
            mail.attach_alternative(html_message, 'text/html')
            mail.send()


    return render(request, 'accounts/reset_password.html')


@login_required(login_url='login')
def list_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'pages/users/list.html', context)


@login_required(login_url='login')
def add_user(request):
    groups = Group.objects.all()
    sites = Site.objects.all()
    agences = Agence.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = username_generator()
            email = form.cleaned_data['email']
            user.save()
            groups = form.cleaned_data['groups']        
            groups.user_set.add(user)
            site = form.cleaned_data['site']
            user.site.add(site)

            subject = "Création de compte"
            email_template_name = "partials/mails/user_creation.html"
            ctxt = {
                "name": user.first_name,
                "link": "http://127.0.0.1:8000/accounts/set_password/" + str(user.username) + "/"
            }
            html_message = render_to_string(email_template_name, ctxt)
            plain_message = strip_tags(html_message)
            mail = EmailMultiAlternatives(
                subject,
                plain_message,
                'OMILAYE <euphrem0427@gmail.com>' ,
                [email]
            )
            mail.attach_alternative(html_message, 'text/html')
            mail.send()
            
            return redirect('list_users')
    context ={
        'sites':sites,
        'agences':agences,
        'groups':groups,
    }
    return render(request, 'pages/users/add.html', context)


@unauthentificated_user
def first_login(request, username):

    user = User.objects.get(username=username)
    if request.POST:
        password = request.POST['password1']
        user.set_password(password)
        user.save()
        return redirect('login')
           
    context = {'user': user}
    return render(request, 'accounts/first_login.html', context)


@login_required(login_url='login')
def edit_user(request, id):
    user = User.objects.get(id=id)
    form = EditUserForm(
        instance = user,
        initial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
        }
    )
    if request.method == 'POST':
        form = EditUserForm(
            request.POST,
            instance = user,
            initial = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
            }
        )
        if form.is_valid():
            form.save()
            return redirect('list_users')
    context ={}
    return render(request, 'pages/users/edit.html', context)


@login_required(login_url='login')
def upgrade_user(request, id):
    user = User.objects.get(id=id)
    form = UpgradeUserForm(
        instance = user,
        initial = {
            'agence': user.agence,
            'site': user.site,
            'groups': user.groups,
        }
    )
    if request.method == 'POST':
        form = UpgradeUserForm(
            request.POST,
            instance = user,
            initial = {
                'agence': user.agence,
                'site': user.site,
                'groups': user.groups,
            }
        )
        if form.is_valid():
            form.save()
            return redirect('list_users')
    context ={}
    return render(request, 'pages/users/upgrade.html', context)


@login_required(login_url='login')
def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('list_users')
    


@login_required(login_url='login')
def view_user(request, id):
    user = User.objects.get(id=id)
    context ={
        'user': user
    }
    return render(request, 'pages/users/view.html', context)


################################################################
### GROUP CONFIG
################################################################


@login_required(login_url='login')
def list_groups(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'accounts/group/list.html', context)


@login_required(login_url='login')
def add_group(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_groups')

    context = {}
    return render(request, 'accounts/group/add.html', context)

    
@login_required(login_url='login')
def delete_group(request, id):
    group = Group.objects.get(id=id)
    group.delete()
    return redirect('list_groups')