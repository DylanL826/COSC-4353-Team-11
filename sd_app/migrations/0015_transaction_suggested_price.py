# Generated by Django 3.2.7 on 2022-07-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0014_auto_20220710_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='suggested_price',
            field=models.CharField(default='$1,234', max_length=6),
        ),
    ]
