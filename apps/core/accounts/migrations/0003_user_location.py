# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 17:07
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161107_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
