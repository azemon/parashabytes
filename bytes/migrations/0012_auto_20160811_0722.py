# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytes', '0011_word_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parasha',
            options={'ordering': ['sortkey', 'transliterated_name']},
        ),
        migrations.AddField(
            model_name='parasha',
            name='sortkey',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
