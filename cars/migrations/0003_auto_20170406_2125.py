# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20170406_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacities',
            name='capacity_id',
            field=models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
