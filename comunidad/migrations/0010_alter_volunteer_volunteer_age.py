# Generated by Django 4.2.4 on 2023-09-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0009_alter_organization_organization_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='volunteer_age',
            field=models.PositiveIntegerField(max_length=99),
        ),
    ]
