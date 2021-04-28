from behave import then
from utils import propagate_scope

from yaddy import *


@then("{entity} should have valid python representation of {cls}")
@propagate_scope(__name__)
def step_implementation(context, entity, cls):
    item = eval(entity)
    assert item == eval(repr(item))
