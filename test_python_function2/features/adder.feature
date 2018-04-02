Feature: Adder test

  @smoketest
  Scenario: Check the function add()
    Given The function add is callable
    When I call function add with arguments 1 and 2
    Then I should get 3 as a result

  Scenario Outline: Thorough checking function add()
    Given The function add is callable
    When I call function add with arguments <x> and <y>
    Then I should get <result> as a result

     Examples: users
     |x|y|result|
     # basic arithmetic
     |          0| 0|          0|
     |          1| 2|          3|
     |          1|-2|         -1|
     # no overflows at 16 bit limits
     |      32767| 1|      32768|
     |      65535| 1|      65536|
     # integer overflow in Python?
     | 2147483648| 1| 2147483649|
     |-2147483647|-1|-2147483648|
     |-2147483648|-1|-2147483649|

