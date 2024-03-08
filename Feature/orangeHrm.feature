Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHrm home Page
    Given launch chrome broswer
    When open orange hrm homepage
    Then verify that the logo present on page
    And close browser

    # to run the code on terminal write 'behave file path from context root directory