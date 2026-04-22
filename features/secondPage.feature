Feature: Second page feature
As a software engineer i need a second page
so that i check if life is good like Josh said

Scenario Outline:
    When users send a GET request to /<name>
    Then it returns <name>'s job: <job>

    Examples:
        | name      | job      |
        | Urish     | Manager  |
        | Nomad     | Selenium |
        | Hugh      | Market   |
        | Carl      | Core     |
        