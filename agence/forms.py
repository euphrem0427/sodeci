from django.forms import *
from app.models import *

class AgenceForm(ModelForm):
    
    class Meta:
        model = Agence
        fields = ("title", "description", "adresse", "phone", "email", "departement")

class SiteForm(ModelForm):
    
    class Meta:
        model = Site
        fields = ("agence", "title", "description", "adresse", "departement", "commune")

class AbonneForm(ModelForm):
    
    class Meta:
        model = Abonne
        fields = ("agence", "first_name", "last_name", "adresse", "phone", "ifu", "departement", "commune")


class DepartementForm(ModelForm):
    
    class Meta:
        model = Departement
        fields = ("name",)

class CommuneForm(ModelForm):
    
    class Meta:
        model = Commune
        fields = ("name", "departement")
