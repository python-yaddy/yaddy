from behave import when


@when("I initialize {entity} from {cls} with {arguments}")
def step_implementation(context, entity, cls, arguments):
    class_ = getattr(context, cls)
    kwargs = eval("dict(" + arguments + ")")
    instance = class_(**kwargs)
    setattr(context, entity, instance)
