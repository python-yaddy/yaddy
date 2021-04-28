"""
This module describes Entity class.
"""
from typing import Any, Optional
from uuid import uuid4


class Entity:
    """
    Entity class for DDD.

    Entity is mutable so it has to have an unique identifier
    (uid).
    Entity can be composed from other entities and values.
    """

    uid: str

    def __init__(
        self,
        *,
        uid: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        **kwargs: Any,
    ):
        if uid is None:
            uid = self.uid_factory()
        self.uid = uid
        for field, value in kwargs.items():
            setattr(self, field, value)

    def __repr__(self) -> str:
        fields = self.__annotations__.keys()  # pylint: disable=no-member
        values = ((field, getattr(self, field)) for field in fields)
        parameters = (f"{field}={value!r}" for field, value in values)

        return f"{self.__class__.__name__}({', '.join(parameters)})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uid == other.uid

    @staticmethod
    def uid_factory() -> str:
        """Construct uid if it was not given to the init method."""
        return uuid4().hex
