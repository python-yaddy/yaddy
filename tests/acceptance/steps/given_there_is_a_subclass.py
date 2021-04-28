import sys

from behave import given
from utils import propagate_scope

import yaddy


@given("there is a subclass of {parent} called {child} with fields {fields}")
@propagate_scope(__name__)
def step_implementation(context, parent, child, fields):
    """
    Parent should be accessible to import from yaddy or context

    child class will be created dynamically and put into context
    """

    module = sys.modules[__name__]
    for name, value in context.scope.items():
        value = context.scope[name]
        setattr(module, name, value)

    parent_class = getattr(yaddy, parent)
    fields_dict = {
        field.strip(): eval(type_.strip())
        for field, type_ in map(lambda item: item.split(":"), fields.split(","))
    }

    class_ = type(
        child,
        (parent_class,),
        {
            "__annotations__": fields_dict,
        },
    )

    context.scope[child] = class_


@given("there is a subclass of {parent} called {child}")
@propagate_scope(__name__)
def step_implementation(context, parent, child):
    """
    Parent should be accessible to import from yaddy or context

    child class will be created dynamically and put into context
    """

    parent_class = getattr(yaddy, parent)

    class_ = type(child, (parent_class,), {})

    context.scope[child] = class_
