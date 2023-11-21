# Generated by Django 4.2.4 on 2023-09-17 05:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0012_alter_volunteer_volunteer_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'Ingresa un nombre válido')])),
                ('manager_lastname', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'Ingresa un apellido válido')])),
                ('manager_age', models.IntegerField(validators=[django.core.validators.MinValueValidator(13, message='La edad debe ser mayor a 0.'), django.core.validators.MaxValueValidator(99)])),
                ('manager_mail', models.EmailField(max_length=100, unique=True)),
                ('manager_phone', models.IntegerField(max_length=10)),
                ('manager_password', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 8', regex='^.{8}$')])),
            ],
        ),
    ]
