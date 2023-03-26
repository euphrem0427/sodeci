from .models import *


def get_ph_standard_value(parameterph,ph):

    for j in parameterph:
        if (j['ph']):
            standardph = j['ph']
    tauxph = (ph/standardph)*100
    return tauxph
    

def get_humidity_standard_value(parameterhumidity,humidity):

    for j in parameterhumidity:
        if (j['humidity']):
            standardhumidity = j['humidity']
    tauxhumidity = (humidity/standardhumidity)*100
    return tauxhumidity

def get_chlore_standard_value(parameterchlore,chlore):

    for j in parameterchlore:
        if (j['chlore']):
            standardchlore = j['chlore']
    tauxchlore = (chlore/standardchlore)*100
    return tauxchlore