# Generated by Django 4.2.1 on 2023-05-19 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_property_is_features_alter_property_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='is_features',
        ),
    ]
