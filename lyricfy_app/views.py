# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from lyricfy_app.models import Song, Album


# Create your views here.


def Home(request):
    template = "home.html"
    context = {
        "songs": Song.objects.all()[:10],
        "albums": Album.objects.all()[:10],
    }
    return render(request, template, context)

class Register(CreateView):
    model = User
    template_name = "registration/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
