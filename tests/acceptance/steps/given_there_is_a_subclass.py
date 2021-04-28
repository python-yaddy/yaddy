from behave import given
import yaddy


@given("there is a subclass of {parent} called {child} with fields {fields}")
def step_implementation(context, parent, child, fields):
    """
    Parent should be accessible to import from yaddy

    child class will be created dynamically and put into context
    """

    parent_class = getattr(yaddy, parent)
    fields_dict = {
        field.strip(): eval(type_.strip())
        for field, type_ in map(lambda item: item.split(":"), fields.split(","))
    }

    class_ = type(child, (parent_class, ), {

    })

    for field, type_ in fields_dict.items():
        class_.__annotations__[field] = type_

    setattr(context, child, class_)


@given("there is a subclass of {parent} called {child}")
def step_implementation(context, parent, child):
    """
    Parent should be accessible to import from yaddy

    child class will be created dynamically and put into context
    """
    parent_class = getattr(yaddy, parent)

    class_ = type(child, (parent_class, ), {})

    setattr(context, child, class_)
