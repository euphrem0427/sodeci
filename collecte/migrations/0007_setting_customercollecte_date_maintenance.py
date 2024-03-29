# Generated by Django 4.1.2 on 2023-02-20 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_abonne_date_ajout'),
        ('collecte', '0006_alter_sitecollecte_date_recharge_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, verbose_name='Nom du parametre')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.AddField(
            model_name='customercollecte',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=254, verbose_name='Valuer du paremetre')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collecte.setting')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.site')),
            ],
            options={
                'verbose_name': 'Maintenance',
                'verbose_name_plural': 'Maintenances',
            },
        ),
    ]
