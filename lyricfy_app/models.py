# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return u"%s" % self.name


class Album(models.Model):
    name = models.CharField(max_length=120)
    author = models.ForeignKey(Author)
    songs_number = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.name


class Lyric(models.Model):
    name = models.CharField(max_length=120)
    lyric = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name


class Song(models.Model):
    name = models.CharField(max_length=120)
    authors = models.ForeignKey(Author, null=True, related_name='Autor')
    singer = models.ManyToManyField(Author, related_name='Cantant')
    album = models.ManyToManyField(Album, related_name='Album', blank=True)
    lyric = models.ForeignKey(Lyric, null=True, related_name='Lletra', blank=True)

    def __unicode__(self):
        return u"%s" % self.name

class Playlist(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s" % self.name


class Playlist_Song(models.Model):
    playlist = models.ForeignKey(Playlist, null=True, related_name='Llista_de_reproduccio')
    song = models.ForeignKey(Song, null=True, related_name='Song')

    def __unicode__(self):
        return u"%s" % self.playlist.name + u" - %s" % self.song.name