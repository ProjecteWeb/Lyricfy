# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

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
