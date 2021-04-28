from behave import then
from utils import propagate_scope


@then("{entity}'s {field} is set")
@propagate_scope(__name__)
def step_implementation(context, entity, field):
    item = eval(entity)
    value = getattr(item, field)

    assert value is not None
