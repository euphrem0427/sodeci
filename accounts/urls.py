from django.urls import path
from .views import *
urlpatterns = [
    path('', profil, name = 'profil'),
    path('login/', login, name = 'login'),
    path('reset_password', reset_password, name = 'reset_password'),
]
