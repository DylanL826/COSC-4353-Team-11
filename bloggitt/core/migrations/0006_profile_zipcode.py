# Generated by Django 3.1.2 on 2022-06-26 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220627_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
