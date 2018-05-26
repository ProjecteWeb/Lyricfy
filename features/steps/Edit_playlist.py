from behave import *

use_step_matcher("parse")


@when("I go to MyPlaylist page")
def step_impl(context):
    context.browser.find_by_name('playlist_name').first.click()


@then("I can edit MyPlaylist name to {MyPlaylist1}")
def step_impl(context, MyPlaylist1):
    context.browser.find_by_name('edit_playlist').first.click()

    context.browser.fill("name", MyPlaylist1)
    context.browser.find_by_name("save").click()


@step("I can see the Correct Edition message and go back to see {MyPlaylist1} name")
def step_impl(context, MyPlaylist1):
    # assert context.browser.find_by_name('correct_edition')
    context.browser.find_by_value("goback").click()

    assert context.browser.is_text_present(MyPlaylist1)


@then('I can delete MyPlaylist')
def step_impl(context):
    context.browser.find_by_name('delete_playlist').first.click()

    assert context.browser.is_text_present('eliminat correctament.')


@step('comprove that "MyPlaylist" doesn\'t exists in Plyalists list')
def step_impl(context):
    context.browser.find_by_name("back_to_playlists").click()


@given('Exists song "{FirstSong}"')
def step_impl(context, FirstSong):
    from lyricfy_app.models import Song

    song = Song(name=FirstSong)
    song.save()



@given('Exists a relation Song "{FirstSong}" and "{MyPlaylist}"')
def step_impl(context, FirstSong, MyPlaylist):
    from lyricfy_app.models import Playlist_Song, Song, Playlist
    song = Song.objects.get(name=FirstSong)
    playlist = Playlist.objects.get(name=MyPlaylist)
    playlist_song = Playlist_Song()
    playlist_song.song = song
    playlist_song.playlist = playlist
    playlist_song.save()


@then('I delete song "FirstSong" from "MyPlaylist" and save the changes')
def step_impl(context):
    context.browser.find_by_name('edit_playlist').first.click()
    context.browser.find_by_name('selected_song').first.click()
    context.browser.find_by_name('save').first.click()


@then("I see the delete confirmation of song {FirstSong}")
def step_impl(context, FirstSong):
    context.browser.find_by_value('goback').click()
    assert not context.browser.is_text_present(FirstSong)