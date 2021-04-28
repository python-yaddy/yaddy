Feature: Library provides a value class

  Scenario: Value initialization
    Given there is a subclass of Value called Point
    When I initialize point from Point
    Then point should have valid python representation of Point
