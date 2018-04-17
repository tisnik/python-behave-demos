Feature: Smoke test

  Scenario: Check the REST API service entry point
    Given REST API service is accessible
    When I access the API endpoint /not-existing
    Then I should receive 200 status code

  Scenario: Repeatedly check the REST API service entry point
    Given REST API service is accessible
    When I access the API endpoint /not-existing 5 times with 0 seconds delay
    Then I should get 200 status code for all calls
