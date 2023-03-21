from django.urls import path
from .views import *
urlpatterns = [
    path('site_collect_list/', site_collect_list, name="site_collect_list"),
    path('choice_site_collect/', choice_site_collect, name="choice_site_collect"),
    #path('create_site_collect/<int:id>/', create_site_collect),
    #path('add_site_collect/<int:id>/', add_site_collect),
    path('add_collect_on_site/<int:id>/', add_collect_on_site),
    path('view_site_collect/<int:id>/', view_site_collect),
    path('delete_site_collect/<int:id>/', delete_site_collect),

    path('list_setting/', list_settings, name="list_setting"),
    path('add_setting/', add_setting, name="add_setting"),
    path('view_setting/<int:id>/', view_setting),
    path('delete_setting/<int:id>/', delete_setting),

    path('list_site_setting/', list_site_settings, name="list_site_setting"),
    path('add_site_setting/', add_site_setting, name="add_site_setting"),
    path('view_site_setting/<int:id>/', view_site_setting),
    path('delete_site_setting/<int:id>/', delete_site_setting),

    path('list_maintenance/', list_maintenance, name="list_maintenance"),
    path('add_maintenance/<int:id>/', add_maintenance),
    path('create_maintenance/<int:id>/', create_maintenance),
    path('choice_maintenance_site', choice_maintenance_site, name="choice_maintenance_site"),
    path('view_maintenance/<int:id>/', view_maintenance),
    path('delete_maintenance/<int:id>/', delete_maintenance),

    path('list_customer_collecte/', list_customer_collecte, name="list_customer_collecte"),
    path('add_customer_collecte/<int:id>/', add_customer_collecte),
    path('delete_customer_collecte/<int:id>/', delete_customer_collecte),
    path('view_customer_collecte/<int:id>/', view_customer_collecte),
    path('choice_customer',choice_customer, name ="choice_customer"),
]