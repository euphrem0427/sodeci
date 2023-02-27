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
