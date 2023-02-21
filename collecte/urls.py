from django.urls import path
from .views import *
urlpatterns = [
    path('site_collect_list/', site_collect_list, name="site_collect_list"),
    path('choice_site_collect/', choice_site_collect, name="choice_site_collect"),
    path('add_site_collect/<int:id>/', add_site_collect),
    path('view_site_collect/<int:id>/', view_site_collect),

    path('list_setting/', list_settings, name="list_setting"),
    path('add_setting/', add_setting, name="add_setting"),
    path('view_setting/<int:id>/', view_setting),
    path('delete_setting/<int:id>/', delete_setting),

    path('list_maintenance/', list_maintenance, name="list_maintenance"),
    path('add_maintenance/<int:id>/', add_maintenance),
    path('create_maintenance/<int:id>/', create_maintenance),
    path('choice_maintenance_site', choice_maintenance_site, name="choice_maintenance_site"),

    
]