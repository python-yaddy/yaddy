"""
This module describes Entity class.
"""
from typing import Any, Dict, Optional
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
        uid: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ):
        if uid is None:
            uid = self.uid_factory()
        self.uid = uid
        for field, value in kwargs.items():
            setattr(self, field, value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(uid={self.uid!r})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.uid == other.uid

    @staticmethod
    def uid_factory() -> str:
        """Construct uid if it was not given to the init method."""
        return uuid4().hex
