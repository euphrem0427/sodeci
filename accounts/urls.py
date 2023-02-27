from django.urls import path
from .views import *
urlpatterns = [
    path('', profil, name = 'profil'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name='logout'),
    path('set_password/<str:username>/', first_login),
    path('reset_password', reset_password, name = 'reset_password'),

    path('list_groups/', list_groups, name = 'list_groups'),
    path('add_group/', add_group, name = 'add_group'),
    path('delete_group/<int:id>/', delete_group),

    path('list_users', list_users, name = 'list_users'),
    path('add_user', add_user, name = 'add_user'),
    path('edit_user/<int:id>/', edit_user),
    path('delete_user/<int:id>/', delete_user),
    path('upgrade_user/<int:id>/', upgrade_user),
    path('view_user/<int:id>/', view_user),
]
