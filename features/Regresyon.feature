Feature: Contact Policy Test
  Scenario: Call GetOffer Request and check ih record is exist
    Given Call GetOffer Request
    When IH record is exist
    Then Scenario is successfully completed