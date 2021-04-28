Feature: Library provides an entity class

  Scenario: Entity initialization
    Given there is a subclass of Entity called Model
    When I initialize model from Model with uid="some identifier"
    Then model should have valid python representation of Model

  Scenario: Entity subclassing
    Given there is a subclass of Entity called Author with fields name: str
    When I initialize author from Author with name="Edgar Alan Poe"
    Then author should have valid python representation of Author
    And author's uid is set
    And author's name is set
