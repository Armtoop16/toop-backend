# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 16:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0004_auto_20161107_1627'),
        ('accounts', '0004_connection_gift_lists'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connection',
            name='social_account',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialAccount'),
            preserve_default=False,
        ),
    ]
