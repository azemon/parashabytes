# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bytes', '0004_auto_20160624_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='book',
        ),
        migrations.RemoveField(
            model_name='word',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='word',
            name='sortkey',
        ),
        migrations.RemoveField(
            model_name='word',
            name='verse',
        ),
    ]