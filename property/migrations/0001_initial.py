# Generated by Django 4.2.1 on 2023-05-19 17:04

import ckeditor.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('price', models.IntegerField()),
                ('property_id', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('property_type', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=30)),
                ('bed', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('property_description', ckeditor.fields.RichTextField()),
                ('amentities', multiselectfield.db.fields.MultiSelectField(choices=[('Balcony', 'Balcony'), ('Outdoor Kitchen', 'Outdoor Kitchen'), ('Cable Tv', 'Cable Tv'), ('Deck', 'Deck'), ('Two Parlour', 'Two Parlour'), ('Garden', 'Garden'), ('Tennis Courts', 'Tennis Courts'), ('Internet', 'Internet'), ('Parking', 'Parking'), ('Sun Room', 'Sun Room'), ('Swim House', 'Swim House'), ('Concrete Flooring', 'Concrete Flooring'), ('Tiles', 'Tiles')], max_length=255)),
                ('video', models.FileField(upload_to='video/%Y/%m/%d')),
                ('floor_plan', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
