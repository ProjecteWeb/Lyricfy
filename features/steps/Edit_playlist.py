from behave import *

use_step_matcher("parse")


@when("I go to MyPlaylist page")
def step_impl(context):
    context.browser.find_by_name('playlist_name').first.click()


@then("I can edit MyPlaylist name to {MyPlaylist1}")
def step_impl(context, MyPlaylist1):
    context.browser.find_by_name('edit_playlist').first.click()

    context.browser.fill("name", MyPlaylist1)
    context.browser.find_by_name('save').first.click()


@step("I can see the Correct Edition message and go back to see {MyPlaylist1} name")
def step_impl(context, MyPlaylist1):
    assert context.browser.find_by_name('correct_edition')
    context.browser.find_by_name('go_back_to_playlists').first.click()

    assert context.browser.is_text_present(MyPlaylist1)