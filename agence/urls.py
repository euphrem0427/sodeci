from django.urls import path
from .views import *

urlpatterns = [
    # Agence URLs
    path('agence_list', agence_list, name = 'agence_list'),
    path('add_agence', add_agence, name = 'add_agence'),
    path('edit_agence/<int:id>/', edit_agence),
    path('delete_agence/<int:id>/', delete_agence),
    path('view_agence/<int:id>/', view_agence),

    #Site URLs
    path('site_list', site_list, name = 'site_list'),
    path('add_site', add_site, name = 'add_site'),
    path('delete_site/<int:id>/', delete_site),
    path('edit_site/<int:id>/', edit_site),
    path('view_site/<int:id>/', view_site),
]
