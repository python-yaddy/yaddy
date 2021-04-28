from yaddy.domain_object import DomainObject


def test_entity_subclassing_generates_default_initializer_based_on_annotations():
    class Author(DomainObject):

        name: str

    name = "Edgar Alan Poe"
    author = Author(name=name)
    assert author.name == name


def test_entity_subclassing_automatically_propagates_parameters_to_representation():
    class Author(DomainObject):

        name: str

    name = "Edgar Alan Poe"
    author = Author(name=name)
    assert name in str(author)


def test_asdict_method_returns_dictionary_for_entity():
    class Author(DomainObject):

        name: str

    name = "Edgar Alan Poe"
    author = Author(name=name, uid="1")
    assert author.asdict() == {"uid": "1", "name": name}
