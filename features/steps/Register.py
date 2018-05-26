from behave import *

use_step_matcher("parse")


@given('I sign up completing the fields as user "{user1}" with password "{password}"')
def step_impl(context, user1, password):
    context.browser.visit(context.get_url('/lyricfy_app/Registre/'))

    context.browser.fill('username', user1)
    context.browser.fill('password1', password)
    context.browser.fill('password2', password)
    context.browser.find_by_id('registration').first.click()


@when('I sign up completing the fields as user "{user1}" with password "{password}"')
def step_impl(context, user1, password):
    context.browser.visit(context.get_url('/lyricfy_app/Registre/'))

    context.browser.fill('username', user1)
    context.browser.fill('password1', password)
    context.browser.fill('password2', password)
    context.browser.find_by_id('registration').first.click()


@then("There is an error because the user allready exists")
def step_impl(context):
    assert context.browser.find_by_text('Ja existeix un usuari amb aquest nom.')


@when('I try to sign up with "{user2}" using password "{password}" with password confirmation "{password1}"')
def step_impl(context, user2, password, password1):
    context.browser.visit(context.get_url('/lyricfy_app/Registre/'))

    context.browser.fill('username', user2)
    context.browser.fill('password1', password)
    context.browser.fill('password2', password1)
    context.browser.find_by_id('registration').first.click()


@then("There is as error because I use two different passwords")
def step_impl(context):
    assert context.browser.find_by_text('Els dos camps de contrasenya no coincideixen.')
