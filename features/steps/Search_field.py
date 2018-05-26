from behave import *

use_step_matcher("parse")


@given("I'm on the initial page of the application")
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/'))


@when('I search the song "{song}"')
def step_impl(context, song):
    context.browser.fill('song', song)
    form = context.browser.find_by_tag('form').first
    form.find_by_value('search').first.click()


@then("I obtain a list with all the relationed names of songs")
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/search?name=Boom'))


@when('I search the artist "{artist}"')
def step_impl(context, artist):
    context.browser.fill('song', artist)
    form = context.browser.find_by_tag('form').first
    form.find_by_value('search').first.click()


@then('I obtain a list with all the songs and albums of Shakira')
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/search?name=Shakira'))


@when('I search the album "{album}"')
def step_impl(context, album):
    context.browser.fill('song', album)
    form = context.browser.find_by_tag('form').first
    form.find_by_value('search').first.click()


@then("I obtain a list with all the albums whit the same name")
def step_impl(context):
    context.browser.visit(context.get_url('/lyricfy_app/search?name=El+Dorado'))


@then("I get a message that there is no song with this name")
def step_impl(context):
    assert context.browser.find_by_id('no_song_found')