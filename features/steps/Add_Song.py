from behave import *

use_step_matcher("re")


@then('I see the songs list that contained "Perfect"')
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/search?song=Perfect'))


@step("I press one song from the list")
def step_impl(context):
    context.browser.find_link_by_partial_text('Perfect').first.click()


@step("I can add this song to MyPlaylist")
def step_impl(context):
    context.browser.find_by_name('add_song').first.click()
    context.browser.find_by_name('selected_playlist').first.click()
    context.browser.find_by_name('add_song').first.click()
