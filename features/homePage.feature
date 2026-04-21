Feature: Home page in the web application
    As a Product Owner
    I want to have a home page that users interact with
    So that I can provide them with a good user experience and easy navigation

    Scenario: User lands on the home page
    Given The website's running
    When The user reches the default route: /
    Then the website returns the home page
    And the home page contains the text: Welcome!
    And the home page contains the text: This is the home page.