# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 18:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_auto_20170212_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickupdate',
            name='collectors',
            field=models.ManyToManyField(related_name='pickup_dates', to=settings.AUTH_USER_MODEL),
        ),
    ]
