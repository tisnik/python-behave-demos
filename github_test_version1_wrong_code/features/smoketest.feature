Feature: Smoke test

  @smoketest
  Scenario: Check the GitHub API entry point
    Given GitHub is accessible
    When I access the API endpoint /
    Then I should receive 404 status code
