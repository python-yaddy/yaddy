import sys
from functools import wraps


def propagate_scope(module_name):
    def decorator(f):
        @wraps(f)
        def wrapper(context, *args, **kwargs):
            module = sys.modules[module_name]
            for name, value in context.scope.items():
                value = context.scope[name]
                setattr(module, name, value)
            f(context, *args, **kwargs)

        return wrapper

    return decorator
