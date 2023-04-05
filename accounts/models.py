from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from app.models import *
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

    site = models.ManyToManyField(
        Site,
        blank = True,
        verbose_name = _('Site'),
    )
    

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'



class StatusHistory(models.Model):

    abonne = models.ForeignKey(
        Abonne,
        on_delete = models.CASCADE,
    )

    status = models.ForeignKey(
        StatusAb,
        on_delete=models.CASCADE,
    )

    agent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("StatusHistory")
        verbose_name_plural = _("StatusHistorys")

    def __str__(self):
        return str(self.status)

    def get_absolute_url(self):
        return reverse("StatusHistory_detail", kwargs={"pk": self.pk})
