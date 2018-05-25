from behave import *

use_step_matcher("parse")


@then("I go to Playlists section")
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/Playlists/'))


@step("I push the button Create playlist")
def step_impl(context):
    context.browser.find_by_tag('button').first.click()


@then('I create a playlist "{MyPlaylist}" for "{user2}"')
def step_impl(context, MyPlaylist, user2):
    context.browser.fill("name", MyPlaylist)
    from django.contrib.auth.models import User
    from lyricfy_app.models import Playlist
    playlist = Playlist()
    playlist.user = User.objects.get(username=user2)
    playlist.name = MyPlaylist
    playlist.save()

    context.browser.find_by_tag('button').first.click()

    context.browser.visit(context.get_url('playlists'))

    assert context.browser.is_text_present(MyPlaylist)


@step("I go to MyPlaylists and there are {count:n} playlist")
def step_impl(context, count):
    from lyricfy_app.models import Playlist
    assert count == Playlist.objects.count()
