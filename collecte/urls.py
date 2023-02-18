from django.urls import path
from .views import *
urlpatterns = [
    path('site_collect_list/', site_collect_list, name="site_collect_list"),
    path('choice_site_collect/', choice_site_collect, name="choice_site_collect"),
    path('add_site_collect/<int:id>/', add_site_collect),
    path('view_site_collect/<int:id>/', view_site_collect),
]