# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-26 19:00
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lyricfy_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='Album', to='lyricfy_app.Album'),
        ),
    ]