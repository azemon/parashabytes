# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bytes', '0003_auto_20160624_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['sortkey']},
        ),
    ]