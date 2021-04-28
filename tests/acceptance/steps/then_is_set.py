from behave import then


@then("{entity}'s {field} is set")
def step_implementation(context, entity, field):
    item = getattr(context, entity)
    value = getattr(item, field)

    assert value is not None
