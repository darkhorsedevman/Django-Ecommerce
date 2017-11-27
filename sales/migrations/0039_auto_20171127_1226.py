# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-27 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0038_pricelist_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelist',
            name='currency',
            field=models.CharField(choices=[(b'EUR', b'EUR'), (b'USD', b'USD'), (b'GBP', b'GBP')], default='EUR', max_length=3),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='customer_type',
            field=models.CharField(choices=[(b'DROP', b'Drop-Shipping'), (b'CLAS', b'Classic')], default='CLAS', max_length=4),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Default pricelist is none is known'),
        ),
    ]
