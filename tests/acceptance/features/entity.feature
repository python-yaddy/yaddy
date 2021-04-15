Feature: Library provides an entity class

  Scenario: Entity initialization
    Given There is a subclass of Entity called Model
    When I initialize model from Model with uid="some identifier"
    Then model should have valid python representation of a Model
