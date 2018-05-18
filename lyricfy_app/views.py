# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from lyricfy_app.forms import PlaylistForm
from models import Playlist


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


def Playlist_profile(request, playlist_name, username):
    return
