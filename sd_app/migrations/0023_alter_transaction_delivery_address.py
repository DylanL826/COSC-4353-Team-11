# Generated by Django 3.2.7 on 2022-07-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0022_alter_transaction_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='delivery_address',
            field=models.CharField(default='PROFILE ADDRESS', max_length=35),
        ),
    ]