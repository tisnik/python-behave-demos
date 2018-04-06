Feature: Sum function test 1

  Scenario: Check the function sum()
    Given a list of integers
      |value |
      | 1    |
      | 10   |
      | 100  |
      | 1000 |
    When I summarize all those integers
    Then I should get 1111 as a result


  Scenario: Check the function sum() for two inputs only
    Given a list of integers
      |value |
      | 1    |
      | 2    |
    When I summarize all those integers
    Then I should get 3 as a result


  Scenario: Check the function sum() for one input only
    Given a list of integers
      |value |
      | 42   |
    When I summarize all those integers
    Then I should get 42 as a result
