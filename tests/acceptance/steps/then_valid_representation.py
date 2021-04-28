from behave import then
from yaddy import *


@then("{entity} should have valid python representation of {cls}")
def step_implementation(context, entity, cls):
    item = getattr(context, entity)
    vars()[cls] = getattr(context, cls)
    assert item == eval(repr(item))
