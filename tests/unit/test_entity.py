import pytest
from uuid import uuid4
from yaddy import Entity


def test_entity_generates_uid_on_creation():
    entity = Entity()

    assert entity.uid


def test_repr_of_an_entity_contains_its_uid():
    entity = Entity()

    assert repr(entity.uid) in repr(entity)


def test_two_different_entities_are_not_equal():
    entity_one = Entity()
    entity_two = Entity()

    assert entity_one != entity_two


def test_two_entities_with_same_uid_are_equal():
    uid = uuid4().hex
    entity_one = Entity(uid=uid)
    entity_two = Entity(uid=uid)

    assert entity_one == entity_two


def test_entity_subclassing_generates_default_initializer_based_on_annotations():
    class Author(Entity):

        name: str

    name = "Edgar Alan Poe"
    author = Author(name=name)
    assert author.name == name
