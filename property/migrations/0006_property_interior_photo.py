# Generated by Django 4.2.1 on 2023-05-22 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_property_is_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='interior_photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photo/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
