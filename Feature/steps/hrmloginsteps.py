from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open HRM Homepage')
def openUrl(context):
    context.driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")


@when('Enter username "{user}" and password "{pwd}"')
def givelogindetails(context, user, pwd):
    context.driver.find_element(By.ID, "txtUsername").send_keys(user)
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)


@when('Click on login button')
def clickLogin(context):
    context.driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()


#  this is for scenario only
# @then('User must successfully login to the Dashboard page')
# def verifyHomepage(context):
#     # text=context.driver.find_element(By.XPATH,"").text
#     # assert text=="Dashboard"
#     context.driver.close()

# this for scenario outline
@then('User must successfully login to the Dashboard page')
def verifyHomepage(context):
    try:
        text = context.driver.find_element(By.XPATH, "").text
    except:
        context.driver.close()
        assert False, "Test Failed"
        # assert text=="Dashboard"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
