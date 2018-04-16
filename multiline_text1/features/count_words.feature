Feature: Count words function test

  Scenario: Check the function count_words()
    Given a sample text
       """
       Velmi kratka veta.
       """
    When I count all words in text
    Then I should get 3 as a result

  Scenario: Check the function count_words()
    Given a sample text
       """
       Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
       eiusmod tempor incididunt ut labore et dolore magna aliqua.
       """
    When I count all words in text
    Then I should get 19 as a result
