# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20161127_1627'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='connection',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='connection',
            name='social_account',
        ),
        migrations.DeleteModel(
            name='Gift',
        ),
        migrations.RemoveField(
            model_name='lists',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
        migrations.DeleteModel(
            name='Lists',
        ),
    ]