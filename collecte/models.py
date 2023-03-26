from time import timezone
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
        null = True,
        blank=True
    )
    image = models.ImageField(_("Image"), upload_to='collecte/abonne')
    date = models.DateTimeField(auto_now_add=True, null = True)

    class Meta:
        verbose_name = _("Collecte Client")
        verbose_name_plural = _("Collectes Client")

    def __str__(self):
        return str(self.abonne.first_name) + " " + str(self.abonne.last_name)

    def get_absolute_url(self):
        return reverse("Site_Collecte_detail", kwargs={"pk": self.pk})



class Setting(models.Model):

    title = models.CharField(max_length=254, verbose_name=_("Nom du parametre"))
    description = models.TextField(_("Description"), null=True, blank=True)

    class Meta:
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Setting_detail", kwargs={"pk": self.pk})

class Maintenance(models.Model):

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE
    )

    agent = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.SET_NULL,
        null = True,
    )
    
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Maintenance")
        verbose_name_plural = _("Maintenances")

    def __str__(self):
        return str(self.site)

    def get_absolute_url(self):
        return reverse("Maintenance_detail", kwargs={"pk": self.pk})


class MaintenanceDetail(models.Model):

    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    
    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE
    )
    value = models.CharField(_("Valuer du paremetre"), max_length=254)
    
    is_exist = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("MaintenanceDetail")
        verbose_name_plural = _("MaintenanceDetails")

    def __str__(self):
        return str(self.maintenance)

    def get_absolute_url(self):
        return reverse("MaintenanceDetail_detail", kwargs={"pk": self.pk})

class SettingSite(models.Model):

    title = models.CharField(max_length=254, verbose_name=_("Nom du parametre"))
    description = models.TextField(_("Description"), null=True, blank=True)

    class Meta:
        verbose_name = _("SettingSite")
        verbose_name_plural = _("SettingSites")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SettingSite_detail", kwargs={"pk": self.pk})


class SiteCollecte(models.Model):

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE
    )

    agent = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.SET_NULL,
        null = True,
    )
    
    date = models.DateTimeField(auto_now_add=True, null = True, blank=True)

    class Meta:
        verbose_name = _("Collecte de site")
        verbose_name_plural = _("Collectes de site")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Site_Collecte_detail", kwargs={"pk": self.pk})

class SiteCollecteDetail(models.Model):

    site_collecte = models.ForeignKey(SiteCollecte, on_delete=models.CASCADE, null = True, blank = True)
    
    setting = models.ForeignKey(
        SettingSite,
        on_delete=models.CASCADE
    )
    value = models.CharField(_("Valuer du paremetre"), max_length=254)
    is_exist = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("SiteCollecteDetail")
        verbose_name_plural = _("SiteCollecteDetails")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SiteCollecteDetail_detail", kwargs={"pk": self.pk})

class WaterQuality(models.Model):

    ph_in_site = models.FloatField(null = True, blank = True)
    humidity_in_site = models.FloatField(null = True, blank = True)
    chlore_in_site = models.FloatField(null = True, blank = True)
    ph_out_site = models.FloatField(null = True, blank = True)
    humidity_out_site = models.FloatField(null = True, blank = True)
    chlore_out_site = models.FloatField(null = True, blank = True)
    date_time = models.DateTimeField(auto_now_add=True, null = True, blank = True)

    class Meta:
        verbose_name = _("WaterQuality")
        verbose_name_plural = _("WaterQualitys")

    def __str__(self):
        return self.ph_in_site

    def get_absolute_url(self):
        return reverse("WaterQuality_detail", kwargs={"pk": self.pk})


class CollectOnSite(models.Model):

    agent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        null = True
    )
    solaire = models.CharField(max_length=100, null=True)
    groupe_electro = models.CharField(max_length=100, null=True)
    index= models.IntegerField(null=True)
    #production = models.CharField(max_length=100, null=True)
    sbee = models.CharField(max_length=100, null=True)
    water_quality = models.ForeignKey(
        WaterQuality,
        on_delete=models.CASCADE,
        null = True
        )
    observation = models.TextField(null = True)
    nbre_panne = models.IntegerField(null = True)
    description_panne = models.TextField(null = True)
    production_estimer = models.CharField(max_length=100,null = True)
    autres= models.TextField(null=True)
    date = models.DateField(auto_now_add=True,null = True)
    class Meta:
        verbose_name = _("CollectOnSite")
        verbose_name_plural = _("CollectOnSites")

    def __str__(self):
        return str(self.site.title)

    def get_absolute_url(self):
        return reverse("CollectOnSite_detail", kwargs={"pk": self.pk})
