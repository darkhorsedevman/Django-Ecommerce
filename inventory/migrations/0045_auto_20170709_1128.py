# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0044_auto_20170706_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodelproductiondescription',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/product_models/production_description/images/%Y/%m/%d'),
        ),
    ]
