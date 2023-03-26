from .models import *


def get_ph_standard_value(parameterph):

    for j in parameterph:
        if (j['ph']):
            standardph = j['ph']
    return standardph

def get_humidity_standard_value(parameterhumidity):

    for j in parameterhumidity:
        if (j['humidity']):
            standardhumidity = j['humidity']
    return standardhumidity

def get_chlore_standard_value(parameterchlore):

    for j in parameterchlore:
        if (j['chlore']):
            standardchlore = j['chlore']
    return standardchlore