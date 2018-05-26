from behave import *

use_step_matcher("parse")


@then("I go to Playlists section")
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/Playlists/'))


@step('I create a playlist "{MyPlaylist}" for "{user2}"')
def step_impl(context, MyPlaylist, user2):
    context.browser.find_by_name('create_playlist').first.click()
    context.browser.find_by_id('id_name').fill(MyPlaylist)
    context.browser.find_by_name('create_playlist').first.click()

    context.browser.visit(context.get_url('playlists'))

    assert context.browser.is_text_present(MyPlaylist)


@step("I go to MyPlaylists and there are {count:n} playlists")
def step_impl(context, count):
    from lyricfy_app.models import Playlist
    assert count == Playlist.objects.count()


@when('I create another playlist "{MyPlaylist}" for "{user2}"')
def step_impl(context, MyPlaylist, user2):
    context.browser.find_by_name('create_playlist').first.click()
    context.browser.find_by_id('id_name').fill(MyPlaylist)
    context.browser.find_by_name('create_playlist').first.click()


@then("I get an error message")
def step_impl(context):
    assert context.browser.is_text_present('El nom de la playlist ja existeix')
