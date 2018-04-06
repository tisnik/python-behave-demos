Feature: Exchange rate test

  Scenario: Check the exchange rate calculation
    Given the following exchange rate table
      | currency |  rate  |
      | CZK      |  1.000 |
      | CAD      | 16.172 |
      | HRK      |  3.407 | 
      | USD      | 20.655 |
    When I sell 10 CAD
    Then I should receive 161.72 CZK

  Scenario: Check the exchange rate calculation
    Given the following exchange rate table
      | currency |  rate  |
      | CZK      |  1.000 |
      | CAD      | 16.172 |
      | HRK      |  3.407 | 
      | USD      | 20.655 |
    When I sell 1 HRK
    Then I should receive 3.407 CZK
    When I sell 2 HRK
    Then I should receive 6.814 CZK

  Scenario: Check the exchange rate calculation
    Given the following exchange rate table
      | currency |  rate  |
      | CZK      |  1.000 |
      | CAD      | 16.172 |
      | HRK      |  3.407 | 
      | USD      | 20.655 |
    When I sell 1000 CZK
    Then I should receive 1000 CZK
