from django.conf.urls import url
from django.views.generic import TemplateView

from lyricfy_app import views

urlpatterns = [
    url(r'^Inici/$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^Registre/$', views.Register.as_view(), name="registre"),
    url(r'^Playlists/$', views.Playlists, name="playlists"),
]
