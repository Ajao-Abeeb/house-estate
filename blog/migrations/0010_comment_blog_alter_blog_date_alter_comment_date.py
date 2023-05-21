# Generated by Django 4.2.1 on 2023-05-18 17:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_comment_blog_alter_blog_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 18, 31, 38, 927714)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 18, 31, 38, 931712)),
        ),
    ]