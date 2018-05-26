# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from lyricfy_app import lyricapi
from lyricfy_app import spotiapi
from lyricfy_app.forms import PlaylistForm
from lyricfy_app.models import *


# Create your views here.

class Register(CreateView):
    model = User
    template_name = "registration/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


def Playlists(request):
    template = 'Playlist/Playlists.html'
    context = {
        "playlists": Playlist.objects.filter(user=request.user)
    }
    return render(request, template, context)


def CreatePlaylist(request):
    template = 'Playlist/CreatePlaylist.html'
    context = {}
    if request.method == 'POST':
        form = PlaylistForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            if (Playlist.objects.filter(user=request.user, name=form.clean_name())):
                template = 'Playlist/IncorrectCreationPlaylist.html'
            else:
                playlist = Playlist()
                playlist.name = form.clean_name()
                playlist.user = request.user
                playlist.save()
                context = {"playlist": playlist}
                template = 'Playlist/CorrectCreationPlaylist.html'
    else:
        context = {
            "form": PlaylistForm()
        }
    return render(request, template, context)


def Playlist_profile(request):
    template = 'Playlist/Info_Playlist.html'

    context = {
        "playlist": Playlist.objects.get(name=request.GET.get('playlist'), user=request.user),
        "songs": Playlist_Song.objects.filter(
            playlist=Playlist.objects.get(name=request.GET.get('playlist'), user=request.user)),
    }
    return render(request, template, context)


def Edit_Playlist(request):
    template = 'Playlist/Edit_Playlist.html'
    context = {
        "playlist": Playlist.objects.get(name=request.GET.get('playlist'), user=request.user),
        "songs": Playlist_Song.objects.filter(
            playlist=Playlist.objects.get(name=request.GET.get('playlist'), user=request.user)),
    }
    return render(request, template, context)


def Edit(request):
    template = 'Playlist/Edit.html'
    context = {}
    try:
        if request.method == 'POST':
            songs_pk = request.POST.getlist('selected_song')
            var = request.POST.dict()

            playlist = Playlist.objects.get(name=request.GET.get('playlist'),
                                            user=User.objects.get(username=request.user.username))
            playlist.name = var['name']
            playlist.save()

            if len(Playlist.objects.filter(user=request.user, name=var['name'])) > 1:
                playlist.name = request.GET.get('playlist')
                playlist.save()
                template = 'Playlist/IncorrectEditionPlaylist.html'
                context = {"playlist": Playlist.objects.get(name=request.GET.get('playlist'),
                                                            user=User.objects.get(username=request.user.username))}
            else:
                for pk in songs_pk:
                    playlist_song = Playlist_Song.objects.get(playlist=playlist, song=Song.objects.get(pk=pk))
                    playlist_song.delete()

                context = {"playlist": playlist}
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    return render(request, template, context)


def Delete_Playlist(request):
    template = 'Playlist/Correct_Delete.html'
    context = {}
    try:
        if request.method == 'POST':
            playlist = Playlist.objects.get(name=request.GET.get('playlist'), user=request.user)
            context = {'name': playlist.name}
            playlist.delete()
    except Exception as e:
        print("%s (%s)" % (e.args, type(e)))

    return render(request, template, context)


def song_Playlist(request):
    template = 'Songs/SongPlaylist.html'
    try:
        context = {
            'name': request.GET.get('name'),
            'artist': request.GET.get('artist'),
            'album': request.GET.get('album'),
            'lyric': Lyric.objects.get(name=request.GET.get('name'))
        }
    except:
        context = {
            'name': request.GET.get('name'),
            'artist': request.GET.get('artist'),
            'album': request.GET.get('album'),
        }
    return render(request, template, context)


def add_Song(request):
    template = 'Songs/AddSong.html'
    context = {
        "playlists": Playlist.objects.filter(user=request.user),
        "album": request.GET.get('album'),
        "artist": request.GET.get('artist'),
        "name": request.GET.get('name'),
    }
    return render(request, template, context)


def confirm_Add_Song(request):
    template = 'Songs/ConfirmAddSong.html'
    context = {
        'artist': request.GET.get('artist'),
        'album': request.GET.get('album'),
        'name': request.GET.get('name'),
    }
    if request.method == 'POST':
        playlist_pk = request.POST.getlist('selected_playlist')
        if playlist_pk:
            if not Lyric.objects.filter(name=context['name']):
                lyrics = lyricapi.get_lyrics(context['name'], context['artist'])
                if lyrics is not None:
                    lyric = Lyric(name=context['name'], lyric=lyrics)
                    lyric.save()
                else:
                    lyric = None
            else:
                lyric = Lyric.objects.get(name=context['name'])

            if not Author.objects.filter(name=context['artist']):
                artist = Author(name=request.GET.get('artist'))
                artist.save()
            else:
                artist = Author.objects.get(name=context['artist'])

            if not Album.objects.filter(name=context['album'], author=artist):
                album = Album(name=request.GET.get('album'), author=artist)
                album.save()
            else:
                album = Album.objects.get(name=context['album'], author=artist)

            if not Song.objects.filter(name=context['name'], author=artist, album=album):
                song = Song(name=request.GET.get('name'), album=album, author=artist, lyric=lyric)
                song.save()
                # song.album.add(album)
            else:
                song = Song.objects.get(name=context['name'], author=artist)

            for pk in playlist_pk:
                if not Playlist_Song.objects.filter(playlist=Playlist.objects.get(pk=pk), song=song):
                    playlist_song = Playlist_Song(playlist=Playlist.objects.get(pk=pk), song=song)
                    playlist_song.save()

    return render(request, template, context)

# Spotify API

def get_Song(request):
    template = 'Songs/Search.html'
    name = request.GET.get('name')
    spotifyAPI = spotiapi.SpotifyAPI()
    song_list = spotifyAPI.get_song_list(name)
    context = {
        'name': name,
        'song_list': song_list,
    }
    return render(request, template, context)


def info_Song(request):
    template = 'Songs/SongInfo.html'
    context = {
        'name': request.GET.get('name'),
        'artist': request.GET.get('artist'),
        'album': request.GET.get('album'),
    }
    return render(request, template, context)

# Lyric API

def get_Lyric(request):
    template = 'Songs/Lyric.html'
    lyric = lyricapi.get_lyrics(request.GET.get('name'), request.GET.get('artist'))
    context = {
        'name': request.GET.get('name'),
        'artist': request.GET.get('artist'),
        'lyric': lyric,
    }
    return render(request, template, context)
