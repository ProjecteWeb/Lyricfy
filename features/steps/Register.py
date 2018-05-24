from behave import *

use_step_matcher("parse")


@given('I sign up completing the fields as user "{user1}" with password "{password}"')
def step_impl(context, user1, password):
    context.browser.visit(context.get_url('/lyricfy_app/Registre/'))

    context.browser.fill('username', user1)
    context.browser.fill('password1', password)


@step('I repetat the password completing the field with password "{password}"')
def step_impl(context, password):
    context.browser.fill('password2', password)


@when('I save the changes for user "{user1}" with password "{password}"')
def step_impl(context, user1, password):
    context.browser.find_by_value('registration').first.click()
    from django.contrib.auth.models import User
    User.objects.create_user(username=user1, email='user@example.com', password=password)


@then("I go to loggin page")
def step_impl(context):
    context.browser.visit(context.get_url('/login/'))


@step('I login as user "{user1}" with password "{password}"')
def step_impl(context, user1, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form').first

    context.browser.fill('username', user1)
    context.browser.fill('password', password)

    form.find_by_value('login').first.click()

    assert context.browser.is_text_present(user1)
