from django.conf.urls import url
from django.views.generic import TemplateView

from lyricfy_app import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^Inici/$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^Registre/$', views.Register.as_view(), name="registre"),
    url(r'^Playlists/New_Playlist/$', views.CreatePlaylist, name="Create_playlist"),

    url(r'^Playlists/(?P<playlist_name>[\w-]+)/(?P<username>[\w-]+)/Edit_Playlist/$', views.Edit_Playlist,
        name="Edit_playlist"),
    url(r'^Playlists/(?P<playlist_name>[\w-]+)/(?P<username>[\w-]+)/$', views.Playlist_profile, name="playlist"),

    url(r'^Playlists/Delete_Playlist$', views.Delete_Playlist, name="Delete_playlis"),
    url(r'^Playlists/Correct_Edition$', views.Correct_editon, name="Correct_Edition"),
    url(r'^Playlists/$', views.Playlists, name="playlists"),
]
