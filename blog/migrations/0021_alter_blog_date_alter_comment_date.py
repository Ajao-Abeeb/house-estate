# Generated by Django 4.2.1 on 2023-05-20 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_blog_date_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 13, 12, 29, 749403)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 13, 12, 29, 752401)),
        ),
    ]