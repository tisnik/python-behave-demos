Feature: Smoke test

  @smoketest
  Scenario: Check the httpbin.org API entry point
    Given API for httpbin.org is accessible
    When I access the API endpoint /
    Then I should receive 200 status code

  Scenario: Check the httpbin.org API entry point
    Given API for httpbin.org is accessible
    When I access the API endpoint /status/200
    Then I should receive 200 status code

  Scenario: Check the httpbin.org API entry point
    Given API for httpbin.org is accessible
    When I access the API endpoint /status/123
    Then I should receive 123 status code
