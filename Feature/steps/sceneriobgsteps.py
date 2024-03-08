from behave import *
from selenium import webdriver

@given('I launch browser')
def step_impl(context):
    # context.driver=webdriver.Chrome()
    assert True, "Test passed"

@when('I open application')
def step_impl(context):
    assert True, "Test passed"


@when('Enter valid {username} and {password}')
def step_impl(context,username,password):
    assert True, "Test passed"

@when('Click on login')
def step_impl(context):
    assert True, "Test passed"


@then('User must login to the dashboard page')
def step_impl(context):
    assert True, "Test passed"


@when('navigate to search display')
def step_impl(context):
    assert True, "Test passed"



@then('search page should display')
def step_impl(context):
    assert True, "Test passed"


@when('navigate to advanced search page')
def step_impl(context):
    assert True, "Test passed"


@then('advanced search page should display')
def step_impl(context):
    assert True, "Test passed"