Feature: Library provides an entity class

  Scenario: Entity initialization
    Given there is a subclass of Entity called Model
    When I initialize model from Model with uid="some identifier"
    Then model should have valid python representation of Model

  Scenario: Entity subclassing
    Given there is a subclass of Entity called Author with fields name: str, uid: str
    When I initialize author from Author with name="Edgar Alan Poe"
    Then author should have valid python representation of Author
    And author's uid is set
    And author's name is set

  Scenario: Entity serialization as dictionary
    Given there is a subclass of Entity called Author with fields name: str, uid: str
    Given there is a subclass of Entity called Book with fields name: str, author: Author, uid: str
    When I initialize author from Author with name="Edgar Alan Poe", uid=0
    When I initialize book from Book with name="Raven", author=author, uid=1
    Then book should be serialized into dict
    """
    {
      "uid": 1,
      "name": "Raven",
      "author": {
        "uid": 0,
        "name": "Edgar Alan Poe",
      },
    }
    """
