# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bytes', '0005_auto_20160625_1718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Portion',
            new_name='Reading',
        ),
    ]