from django.forms import *


class AgenceForm(forms.ModelForm):
    
    class Meta:
        model = Agence
        fields = ("",)
