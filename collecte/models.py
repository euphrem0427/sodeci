from django.db import models
from accounts.models import *
from app.models import *
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
# Create your models here.

class CustomerCollecte(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.SET_NULL,
        null = True,
    )

    index = models.IntegerField(_("Index"))
    abonne = models.ForeignKey(
        Abonne,
        verbose_name=_("Client"),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(_("Image"), upload_to='collecte/abonne')

    class Meta:
        verbose_name = _("Collecte Client")
        verbose_name_plural = _("Collectes Client")

    def __str__(self):
        return str(self.abonne.first_name) + " " + str(self.abonne.last_name)

    def get_absolute_url(self):
        return reverse("Site_Collecte_detail", kwargs={"pk": self.pk})


class SiteCollecte(models.Model):

    site = models.ForeignKey(
        Site,
        on_delete = models.CASCADE,
        null = True,
    )
    agent = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.SET_NULL,
        null = True,
    )
    date_collecte = models.DateField(auto_now=True)
    qte_gazoil = models.IntegerField()
    date_recharge = models.DateField()
    qte_chlore = models.IntegerField()
    qte_filtre_air = models.IntegerField()
    date_rplment_fitre_air = models.DateField()


    class Meta:
        verbose_name = _("Collecte de site")
        verbose_name_plural = _("Collectes de site")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Site_Collecte_detail", kwargs={"pk": self.pk})
