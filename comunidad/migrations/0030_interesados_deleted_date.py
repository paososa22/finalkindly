# Generated by Django 4.2.4 on 2023-09-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0029_remove_interesados_confirmar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesados',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]