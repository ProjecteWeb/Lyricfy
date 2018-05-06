# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

class Register(CreateView):
    model = User
    template_name = "registration/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
