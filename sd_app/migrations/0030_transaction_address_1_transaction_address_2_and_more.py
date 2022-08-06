# Generated by Django 4.0.5 on 2022-07-30 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0029_auto_20220725_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='address_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='address_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='state',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='transaction',
            name='zipcode',
            field=models.CharField(default='', max_length=9, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='suggested_price',
            field=models.DecimalField(decimal_places=2, default='1.50', max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total_amount_due',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]