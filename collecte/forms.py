from .models import *
from django.forms import *


class SiteCollecteForm(ModelForm):
    
    class Meta:
        model = SiteCollecte
        fields = (
            "qte_gazoil",
            "date_recharge",
            "qte_chlore",
            "qte_filtre_air",
            "date_rplment_fitre_air",
            )

class SettingForm(ModelForm):
    
    class Meta:
        model = Setting
        fields = ("title", "description",)

