from behave import *

use_step_matcher("parse")


@given('Exists a playlist "{MyPlaylist}" for "{username}"')
def step_impl(context, MyPlaylist, username):
    from django.contrib.auth.models import User
    from lyricfy_app.models import Playlist
    playlist = Playlist()
    playlist.user = User.objects.get(username=username)
    playlist.name = MyPlaylist
    playlist.save()


@then('I\'m viewing playlist "{MyPlaylist}" in playlists page')
def step_impl(context, MyPlaylist):
    context.browser.visit(context.get_url('/lyricfy_app/Playlists/'))
    assert context.browser.is_text_present(MyPlaylist)
