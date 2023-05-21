# Generated by Django 4.2.1 on 2023-05-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_property_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_features',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]
