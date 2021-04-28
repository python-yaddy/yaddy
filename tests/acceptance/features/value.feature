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

  Scenario: Value serialization as dictionary
    Given there is a subclass of Value called Point with fields x: float, y: float
    And there is a subclass of Value called Section with fields a: Point, b: Point
    When I initialize p1 from Point with x=0, y=1
    And I initialize p2 from Point with x=1, y=0
    And I initialize section from Section with a=p1, b=p2
    Then section should be serialized into dict
    """
    {
      "a": {
        "x": 0,
        "y": 1,
      },
      "b": {
        "x": 1,
        "y": 0,
      },
    }
    """
