from behave import when
from utils import propagate_scope


@when("I initialize {entity} from {cls} with {arguments}")
@propagate_scope(__name__)
def step_implementation(context, entity, cls, arguments):
    kwargs = eval("dict(" + arguments + ")")
    instance = eval(cls)(**kwargs)
    context.scope[entity] = instance


@when("I initialize {entity} from {cls}")
@propagate_scope(__name__)
def step_implementation(context, entity, cls):
    instance = eval(cls)()
    context.scope[entity] = instance
