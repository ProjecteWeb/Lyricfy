# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lyricfy_app', '0002_auto_20180413_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Album', to='lyricfy_app.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='lyric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Lletra', to='lyricfy_app.Lyrics'),
        ),
    ]
