# Generated by Django 3.1.2 on 2022-06-26 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
    ]