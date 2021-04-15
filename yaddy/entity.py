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
    """

    def __init__(
        self,
        *,
        uid: Optional[str] = None,
    ):
        if uid is None:
            uid = self.uid_factory()
        self.uid = uid

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
