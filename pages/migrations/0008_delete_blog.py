# Generated by Django 4.2.1 on 2023-05-16 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_blog_alter_agent_about_alter_testimony_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blog',
        ),
    ]
