# Generated by Django 4.1.7 on 2023-03-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collecte', '0019_collectonsite_date_waterquality_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectonsite',
            old_name='index_depart',
            new_name='index',
        ),
    ]
