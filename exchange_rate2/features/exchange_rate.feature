Feature: Exchange rate test

  Scenario Outline: Check the exchange rate calculation
    Given the following exchange rate table
      | currency |  rate  |
      | CZK      |  1.000 |
      | CAD      | 16.172 |
      | HRK      |  3.407 | 
      | USD      | 20.655 |
    When I sell <sold> <currency>
    Then I should receive <amount> CZK

    Examples: sold
        | sold | currency | amount |
        | 1    |   CZK    |    1.000 |
        | 10   |   CZK    |   10.000 |
        | 1    |   CAD    |   16.172 |
        | 100  |   CAD    | 1617.200 |
        | 2    |   HRK    |    6.814 |
