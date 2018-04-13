# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lyricfy_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Album', to='lyricfy_app.Album'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='lyric',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Lletra', to='lyricfy_app.Lyrics'),
            preserve_default=False,
        ),
    ]
