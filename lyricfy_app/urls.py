from django.conf.urls import url
from django.views.generic import TemplateView

from lyricfy_app import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^Registre/$', views.Register.as_view(), name="registre"),
    url(r'^Playlists/New_Playlist/$', views.CreatePlaylist, name="Create_playlist"),

    url(r'^Playlists/Info/Edit_Playlist/$', views.Edit_Playlist, name='Edit_playlist'),
    url(r'^Playlists/Info/$', views.Playlist_profile, name='playlist'),

    url(r'^Playlists/Info/Delete_Playlist/$', views.Delete_Playlist, name="Delete_playlist"),
    url(r'^Playlists/Info/Edit_Playlist/Edit/$', views.Edit, name="Edit"),
    url(r'^Playlists/$', views.Playlists, name="playlists"),
    url(r'^search$', views.get_Song, name="search"),
    url(r'^SongInfo$', views.info_Song, name="SongInfo"),
    url(r'^SongPlaylist$', views.song_Playlist, name="SongPlaylist"),
    url(r'^Lyric$', views.get_Lyric, name="Lyric"),
    url(r'^AddSong$', views.add_Song, name="AddSong"),
    url(r'^ConfirmAddSong$', views.confirm_Add_Song, name="ConfirmAddSong"),
]
