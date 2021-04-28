from behave import then
from utils import propagate_scope


@then("{entity} should be serialized into dict")
@propagate_scope(__name__)
def step_implementation(context, entity):
    actual = eval(entity).asdict()
    expected = eval(context.text)
    assert actual == expected
