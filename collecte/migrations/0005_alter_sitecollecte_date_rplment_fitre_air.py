# Generated by Django 4.1.2 on 2023-02-18 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collecte', '0004_alter_sitecollecte_date_collecte_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecollecte',
            name='date_rplment_fitre_air',
            field=models.DateField(auto_now=True),
        ),
    ]