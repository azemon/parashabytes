# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bytes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parasha',
            options={'ordering': ['transliterated_name']},
        ),
        migrations.RemoveField(
            model_name='parasha',
            name='english_name',
        ),
    ]