# Generated by Django 4.2.4 on 2023-08-26 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0002_organization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='organization_dir',
            new_name='organization_address',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='organization_desc',
            new_name='organization_description',
        ),
    ]