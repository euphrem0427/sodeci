from django.urls import path
from .views import *
urlpatterns = [
    path('', profil, name = 'profil'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name='logout'),
    path('set_password/<str:username>/', first_login),
    path('reset_password', reset_password, name = 'reset_password'),
    path('list_users', list_users, name = 'list_users'),
    path('add_user', add_user, name = 'add_user'),
    path('edit_user', edit_user, name = 'edit_user'),
    path('delete_user', delete_user, name = 'delete_user'),
    path('upgrade_user', upgrade_user, name='upgrade_user'),
    path('view_user', view_user, name = 'view_user'),
]
