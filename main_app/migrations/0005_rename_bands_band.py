# Generated by Django 5.0.1 on 2024-02-06 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_bands_alter_brand_options_alter_brand_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bands',
            new_name='Band',
        ),
    ]
