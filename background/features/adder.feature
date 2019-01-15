Feature: Adder test

  Background:
    Given The system is prepared

  Scenario: Check the function add()
    Given The function add is callable
    When I call function add with arguments 1 and 2
    Then I should get 3 as a result

  Scenario: Check the function add() second time
    Given The function add is callable
    When I call function add with arguments 2 and 3
    Then I should get 5 as a result
