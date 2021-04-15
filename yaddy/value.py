"""
This module describes Value class.
"""
from typing import Any


class Value:
    """
    Value class for DDD.

    Value should be immutable, values are compared by... well, value.
    There are no special identifiers as in Entity.
    """

    def __init__(self) -> None:
        pass

    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return False
        for variable in vars(self):
            if getattr(self, variable) != getattr(other, variable):
                return False
        return True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
