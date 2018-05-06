# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-20 16:30
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lyricfy_app', '0004_auto_20180413_1823'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lyrics',
            new_name='Lyric',
        ),
        migrations.AlterField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(blank=True, related_name='Album', to='lyricfy_app.Album'),
        ),
        migrations.RemoveField(
            model_name='song',
            name='singer',
        ),
        migrations.AddField(
            model_name='song',
            name='singer',
            field=models.ManyToManyField(related_name='Cantant', to='lyricfy_app.Author'),
        ),
    ]
