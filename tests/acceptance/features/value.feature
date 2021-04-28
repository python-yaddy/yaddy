Feature: Library provides a value class

  Scenario: Value initialization
    Given there is a subclass of Value called Point
    When I initialize point from Point
    Then point should have valid python representation of Point

  Scenario: Value subclassing
    Given there is a subclass of Value called Point with fields x: float, y: float
    When I initialize point from Point with x=1, y=2
    Then point should have valid python representation of point
    And point's x is set
    And point's y is set
