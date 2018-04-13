# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

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


class Lyrics(models.Model):
    name = models.CharField(max_length=120)
    lyric = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name

class Song(models.Model):
    name = models.CharField(max_length=120)
    singer = models.ForeignKey(Author, null=True, related_name='Cantant')
    authors = models.ForeignKey(Author, null=True, related_name='Autor')
    album = models.ForeignKey(Album, null=True, related_name='Album', blank=True)
    lyric = models.ForeignKey(Lyrics, null=True, related_name='Lletra', blank=True)
    launch_date= models.DateField()

    def __unicode__(self):
        return u"%s" % self.name


class Playlist(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name


class Playlist_Song(models.Model):
    playlist = models.ForeignKey(Playlist, null=True, related_name='Llista_de_reproduccio')
    song = models.ForeignKey(Song, null=True, related_name='Song')

    def __unicode__(self):
        return u"%s" % self.playlist.name + u" - %s" % self.song.name