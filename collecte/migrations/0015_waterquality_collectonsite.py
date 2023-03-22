# Generated by Django 4.1.2 on 2023-03-19 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collecte', '0014_maintenancedetail_is_exist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_in_site', models.IntegerField()),
                ('humidity_in_site', models.IntegerField()),
                ('chlore_in_site', models.IntegerField()),
                ('ph_out_site', models.IntegerField()),
                ('humidity_out_site', models.IntegerField()),
                ('chlore_out_site', models.IntegerField()),
            ],
            options={
                'verbose_name': 'WaterQuality',
                'verbose_name_plural': 'WaterQualitys',
            },
        ),
        migrations.CreateModel(
            name='CollectOnSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solaire', models.CharField(max_length=100, null=True)),
                ('groupe_electro', models.CharField(max_length=100, null=True)),
                ('index_depart', models.IntegerField(null=True)),
                ('produit_traitement', models.CharField(max_length=100, null=True)),
                ('sbee', models.CharField(max_length=100, null=True)),
                ('observation', models.TextField()),
                ('nbre_panne', models.IntegerField()),
                ('description_panne', models.TextField()),
                ('production_estimer', models.CharField(max_length=100)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('water_quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collecte.waterquality')),
            ],
            options={
                'verbose_name': 'CollectOnSite',
                'verbose_name_plural': 'CollectOnSites',
            },
        ),
    ]
