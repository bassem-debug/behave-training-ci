Feature: Search a specific element in the website

  Scenario: Search PyPI home_page
    Given the user navigates to the PyPi Home page
    When he search for "behave"
    Then he see a search result "behave 1.2.5"