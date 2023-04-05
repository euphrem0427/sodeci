from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from agence.models import Commune, Departement


# Create your models here.


class Agence(models.Model):

    title = models.CharField(_('Title'), max_length=100)
    code = models.CharField(_('Code'), max_length=100, unique=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    adresse = models.CharField(_('Adresse'), null=True, blank=True, max_length=255)
    phone = PhoneNumberField(_('Contact'), null = True, blank = True)
    email  = models.EmailField(_('Email'), null = True, blank = True)
    departement = models.ForeignKey(
        Departement,
        on_delete = models.CASCADE,
        null = True, 
        blank = True
        )


    class Meta:
        verbose_name = _("Agence")
        verbose_name_plural = _("Agences")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Agence_detail", kwargs={"pk": self.pk})


class Site(models.Model):

    agence = models.ForeignKey(
        'Agence',
        on_delete = models.CASCADE,
        verbose_name = _('Agence'),
    )

    title = models.CharField(_('Title'), max_length=100)
    code = models.CharField(_('Code'), max_length=100, unique=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    adresse = models.CharField(_('Adresse'), null=True, blank=True, max_length=255)
    departement = models.ForeignKey(
        Departement,
        on_delete = models.CASCADE,
        null = True, 
        blank = True
        )

    commune = models.ForeignKey(
        Commune,
        on_delete = models.CASCADE,
        null = True, 
        blank = True
        )
    class Meta:
        verbose_name = _("Site")
        verbose_name_plural = _("Sites")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Site_detail", kwargs={"pk": self.pk})

class StatusAb(models.Model):

    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("StatusAb")
        verbose_name_plural = _("StatusAbs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("StatusAb_detail", kwargs={"pk": self.pk})

class Abonne(models.Model):

    status = models.ForeignKey(
        StatusAb,
        on_delete=models.CASCADE,
        null = True,
        blank= True
    )

    agence = models.ForeignKey(
        'Agence',
        on_delete = models.CASCADE,
        verbose_name = _('Agence'),
    )

    departement = models.ForeignKey(
        Departement,
        on_delete = models.CASCADE,
        null = True, 
        blank = True
        )

    commune = models.ForeignKey(
        Commune,
        on_delete = models.CASCADE,
        null = True, 
        blank = True
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ifu = models.CharField(max_length=13)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(_('Contact'), null = True, blank = True)
    date_ajout = models.DateTimeField(auto_now_add=True, null = True, blank = True)

    class Meta:
        verbose_name = _("Abonne")
        verbose_name_plural = _("Abonnes")

    def __str__(self):
        return str (self.first_name) + " " + str(self.last_name)

    def get_absolute_url(self):
        return reverse("Abonne_detail", kwargs={"pk": self.pk})


