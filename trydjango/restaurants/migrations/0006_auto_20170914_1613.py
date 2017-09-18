# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurantlocation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
