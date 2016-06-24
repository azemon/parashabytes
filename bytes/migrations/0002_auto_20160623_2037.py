# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['sortkey']},
        ),
        migrations.AlterModelOptions(
            name='parasha',
            options={'ordering': ['english_name']},
        ),
        migrations.AlterModelOptions(
            name='portion',
            options={'ordering': ['start_sortkey']},
        ),
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['english_word']},
        ),
        migrations.AddField(
            model_name='word_location',
            name='sortkey',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parasha',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='description',
            field=models.CharField(blank=True, default='', max_length=2000),
            preserve_default=False,
        ),
    ]
