Feature: Square area calculation
    As a user
    I want to calculate the area of a square
    So that I can find out how much space it occupies
    
    Scenario: Calculate the area of a square of side length 3
        Given I have a square with side length 3
        When I input its side length
        Then the area should be n squared (n * n) which is 9