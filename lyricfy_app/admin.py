# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

admin.site.register(models.Song)
admin.site.register(models.Author)
admin.site.register(models.Playlist)
admin.site.register(models.Lyrics)
admin.site.register(models.Playlist_Song)

