from django.forms import *
from app.models import *

class AgenceForm(ModelForm):
    
    class Meta:
        model = Agence
        fields = ("title", "description", "adresse", "phone", "email")

class SiteForm(ModelForm):
    
    class Meta:
        model = Site
        fields = ("agence", "title", "description", "adresse")
