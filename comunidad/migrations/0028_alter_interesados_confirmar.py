# Generated by Django 4.2.4 on 2023-09-26 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0027_remove_interesados_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesados',
            name='confirmar',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
