from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class Departement(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Departement")
        verbose_name_plural = _("Departements")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Departement_detail", kwargs={"pk": self.pk})

class Commune(models.Model):

    departement = models.ForeignKey(
        Departement,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Commune")
        verbose_name_plural = _("Communes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Commune_detail", kwargs={"pk": self.pk})
