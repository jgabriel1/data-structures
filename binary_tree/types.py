from abc import ABCMeta, abstractmethod
from typing import Any, Protocol, TypeVar


class Comparable(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        ...
