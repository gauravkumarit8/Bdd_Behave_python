from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome broswer')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def step_impl(context):
    context.driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")


@then('verify that the logo present on page')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, "//*[@id='divLogo']/img").is_displayed()
    assert status is True


@then('close browser')
def step_impl(context):
    context.driver.close()
