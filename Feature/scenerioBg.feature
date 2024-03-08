#Feature:
#  Scenario: Login to HRM Application
#    Given I launch browser
#    When I open application
#    And Enter valid username and password
#    And Click on login
#    Then User must login to the dashboard page
#
#  Scenario: Search user
#    Given I launch browser
#    When I open application
#    And Enter valid username and password
#    And Click on login
#    When navigate to search display
#    Then search page should display
#
#  Scenario: Advanced Search user
#    Given I launch browser
#    When I open application
#    And Enter valid username and password
#    And Click on login
#    When navigate to advanced search page
#    Then advanced search page should display

#               INSTED TO USING REPEATED STEP ALWAYS WRITE ALL THOSE STEPS IN BACKGROUND
Feature:
  Background:
    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on login

  Scenario: Login to HRM Application
    Then User must login to the dashboard page

  Scenario: Search user
    When navigate to search display
    Then search page should display

  Scenario: Advanced Search user
    When navigate to advanced search page
    Then advanced search page should display

#    to generate the report use the command in terminals
#   'behave -f allure_behave.formatter:AllureFormatter -o reports/ {file whose refort to generate, eg Feature/}
#   to convert the report in the html format use the terminal command as behave
#     'allure serve {folder name/}