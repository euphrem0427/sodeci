from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from app.models import Agence, Site
# Create your models here.

class User(AbstractUser):
    phone = PhoneNumberField(unique = True, verbose_name="Téléphone")
    email = models.EmailField(unique = True, null = True, blank = True)
    agence = models.ForeignKey(
        Agence,
        verbose_name = 'Agence',
        related_name = 'agence',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'
