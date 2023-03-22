from .models import *
from django.forms import *


class SettingForm(ModelForm):
    
    class Meta:
        model = Setting
        fields = ("title", "description",)

class SettingSiteForm(ModelForm):
    
    class Meta:
        model = SettingSite
        fields = ("title", "description",)

class CustomerCollecteForm(ModelForm):
    
    class Meta:
        model = CustomerCollecte
        fields = ("index", "image")

class CollectOnSiteForm(ModelForm):
    
    class Meta:
        model = CollectOnSite
        fields = (
            "agent", 
            "solaire",
            "groupe_electro",
            "index_depart",
            "production",
            "sbee",
            "water_quality",
            "observation",
            "nbre_panne",
            "description_panne",
            "production_estimer",
            "autres")


class WaterQualityForm(ModelForm):
    
    class Meta:
        model = WaterQuality
        fields = (
            "ph_in_site",
            "humidity_in_site",
            "chlore_in_site",
            "ph_out_site",
            "humidity_out_site",
            "chlore_out_site"
            )
