Feature: OrangeHRM Login
  Scenario: Login to orangeHRM with valid parameters
    Given launch chrome browser
    When open HRM Homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page

#    username and password should be passed here
  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given I launch chrome browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And click on login button
    Then User must successfully login to the dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |

    # if the steps have the same feature then no need to again define it, but it is new call it