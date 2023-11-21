# Generated by Django 4.2.4 on 2023-09-03 00:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0006_rename_organization_phone_organization_organization_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='organization_name',
            field=models.CharField(max_length=500, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'Ingresa un nombre válido')]),
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_web',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='volunteer_lastname',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'Ingresa un apellido válido')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='volunteer_mail',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='volunteer_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'Ingresa un nombre válido')]),
        ),
    ]