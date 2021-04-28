from yaddy import Value


def test_two_different_values_are_equal():

    value_one = Value()
    value_two = Value()

    assert value_one == value_two


def test_value_subclassing_generates_default_initializer_based_on_annotations():
    class Point(Value):

        x: float
        y: float

    x = 4
    y = 3.5
    point = Point(x=x, y=y)

    assert point.x == x
    assert point.y == y


def test_value_subclassing_automatically_propagates_parameters_to_representation():
    class Point(Value):
        x: float
        y: float

    x = 4
    y = 3.5
    point = Point(x=x, y=y)

    assert repr(x) in repr(point)
    assert repr(y) in repr(point)
