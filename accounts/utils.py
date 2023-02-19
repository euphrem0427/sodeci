from .models import *
import random

def username_generator():
    list = "0123456789"
    t_list = [*list]
    t_code = []
    code = ''
    for i in range(5):
        t_code.append(random.choice(t_list))

    for i in t_code:
        code += i

    code = "user_" + code

    try:
        User.objects.get(code=code)
        username_generator()
    except:
        return code
