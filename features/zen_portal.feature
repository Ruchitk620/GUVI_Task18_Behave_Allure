Feature: GUVI Zen Portal authentication
  As a Zen Portal user
  I want to authenticate and log out
  So that I can securely access the portal

  Background:
    Given the user opens the GUVI Zen Portal login page

  @positive
  Scenario: Successful login
    When the user logs in with valid credentials
    Then the dashboard should be displayed

  @negative
  Scenario: Unsuccessful login
    When the user logs in with invalid credentials
    Then the login error should be displayed

  @validation
  Scenario: Validate username and password input boxes
    Then the username and password input boxes should be visible

  @validation
  Scenario: Validate submit button
    Then the submit button should be visible and enabled

  @logout
  Scenario: Logout after successful login
    When the user logs in with valid credentials
    Then the dashboard should be displayed
    When the user logs out
    Then the login page should be displayed again
