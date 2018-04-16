Feature: Count words function test

  Scenario: Check the function count_words()
    Given a sample text
       """
       Velmi kratka veta.
       """
    When I translate the text to upper case
    Then I should get the following text as a result
       """
       VELMI KRATKA VETA.
       """

  Scenario: Check the function count_words()
    Given a sample text
       """
       Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
       eiusmod tempor incididunt ut labore et dolore magna aliqua.
       """
    When I translate the text to upper case
    Then I should get the following text as a result
       """
       LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISICING ELIT, SED DO
       EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA.
       """
