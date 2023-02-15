from app.models import *
import random

def agence_code():
    list = "0123456789"
    t_list = [*list]
    t_code = []
    code = ''
    for i in range(5):
        t_code.append(random.choice(t_list))

    for i in t_code:
        code += i

    code = "agence_" + code

    try:
        Agence.objects.get(code=code)
        agence_code()
    except:
        return code


def site_code():
    list = "0123456789"
    t_list = [*list]
    t_code = []
    code = ''
    for i in range(5):
        t_code.append(random.choice(t_list))

    for i in t_code:
        code += i

    code = "site_" + code

    try:
        Site.objects.get(code=code)
        site_code()
    except:
        return code