# Generated by Django 4.1.2 on 2023-02-21 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collecte', '0008_alter_setting_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='setting',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='value',
        ),
        migrations.CreateModel(
            name='MaintenanceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=254, verbose_name='Valuer du paremetre')),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collecte.maintenance')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collecte.setting')),
            ],
            options={
                'verbose_name': 'MaintenanceDetail',
                'verbose_name_plural': 'MaintenanceDetails',
            },
        ),
    ]
