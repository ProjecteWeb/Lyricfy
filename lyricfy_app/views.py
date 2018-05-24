# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from lyricfy_app.forms import PlaylistForm
from models import *
from spotiapi import *


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
            playlist=Playlist.objects.get(name=request.GET.get('playlist', ''), user=request.user)),
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


# Spotify API

def get_Song(request):
    template = 'Songs/Search.html'
    spotiapi = SpotifyAPI()
    song_list = spotiapi.get_song_list(request.GET.get('name'))
    context = {
        'song_list': song_list,
    }
    return render(request, template, context)
