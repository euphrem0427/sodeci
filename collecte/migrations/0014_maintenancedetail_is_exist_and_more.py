# Generated by Django 4.1.7 on 2023-03-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collecte', '0013_alter_customercollecte_abonne'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancedetail',
            name='is_exist',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitecollectedetail',
            name='is_exist',
            field=models.BooleanField(default=True),
        ),
    ]
