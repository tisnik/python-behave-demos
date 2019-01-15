Feature: Adder test

  Scenario: Check the function add()
    Given The function add is callable
    When I call function add with arguments 1 and 2
    Then I should get 3 as a result
