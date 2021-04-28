"""
This module describes Entity class.
"""
from typing import Any, Dict, Iterable, Optional
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
        fields = self.fields
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

    @property
    def fields(self) -> Iterable[str]:
        "Return fields for current object"
        fields = self.__annotations__.keys()  # pylint: disable=no-member
        return fields

    def asdict(self) -> Dict[str, Any]:
        """Return dictionary serialization for entity"""
        fields = self.fields
        res = {}
        for field in fields:
            value = getattr(self, field)
            if isinstance(value, Entity):
                value = value.asdict()
            res[field] = value
        return res
