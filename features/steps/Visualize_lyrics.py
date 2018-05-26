from behave import *

use_step_matcher("parse")


@given('I see the songs list that contained "Perfect"')
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/search?name=Perfect'))


@when("I press one song from the list")
def step_impl(context):
    context.browser.find_link_by_partial_text('Perfect').first.click()


@then("I can see the lyrics of the song")
def step_impl(context):
    assert context.browser.find_by_id('content')


@given('I see the songs list that contained "Aaa"')
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/search?name=Aaa'))


@when("I press a song from the list")
def step_impl(context):
    context.browser.find_link_by_partial_text('Aaa').first.click()


@then("I get a message that the song have no lyrics")
def step_impl(context):
    assert context.browser.find_by_id('no_lyrics_found')
