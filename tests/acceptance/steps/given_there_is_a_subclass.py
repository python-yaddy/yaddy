from behave import given
import yaddy


@given("There is a subclass of {parent} called {child}")
def step_implementation(context, parent, child):
    """
    Parent should be accessible to import from yaddy

    child class will be created dynamically and put into context
    """
    parent_class = getattr(yaddy, parent)

    class_ = type(child, (parent_class, ), {})

    setattr(context, child, class_)
