# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0085_auto_20170917_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodelpattern',
            name='pattern_type',
            field=models.CharField(choices=[('FA', 'Fabric'), ('FO', 'Foam'), ('FI', 'Hollow Fibres'), ('FF', 'Fabric and Hollow Fibres')], default='FA', max_length=2),
        ),
    ]