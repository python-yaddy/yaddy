from yaddy import Value


def test_two_different_values_are_equal():

    value_one = Value()
    value_two = Value()

    assert value_one == value_two
