# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytes', '0006_auto_20160625_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='sortkey',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]