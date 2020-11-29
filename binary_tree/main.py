from abc import ABCMeta, abstractmethod
from typing import Any, Generic, Optional, TypeVar


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __gt__(self, other: "Comparable") -> bool:
        ...

    @abstractmethod
    def __lt__(self, other: "Comparable") -> bool:
        ...

    @abstractmethod
    def __eq__(self, other: "Comparable") -> bool:
        ...


T = TypeVar("T", Comparable, Any)


class Node(Generic[T]):

    data: T
    _left: Optional["Node[T]"]
    _right: Optional["Node[T]"]

    def __init__(self, data: T) -> None:
        self.data = data
        self._left = None
        self._right = None

    def get_left(self) -> Optional["Node[T]"]:
        return self._left

    def set_left(self, left: "Node[T]") -> None:
        self._left = left

    def get_right(self) -> Optional["Node[T]"]:
        return self._right

    def set_right(self, right: "Node[T]") -> None:
        self._right = right


class BinaryTree(Generic[T]):

    _root: Optional[Node[T]]

    def __init__(self) -> None:
        self._root = None

    def __contains__(self, value: T) -> bool:
        return self.contains(value)

    def insert(self, value: T) -> None:
        current = self._root

        if current is None:
            self._root = Node(value)
            return

        while True:
            if value < current.data:
                if current.get_left() is None:
                    current.set_left(Node(value))
                    break
                else:
                    current = current.get_left()
            elif value > current.data:
                if current.get_right() is None:
                    current.set_right(Node(value))
                    break
                else:
                    current = current.get_right()
            else:
                break

    def contains(self, value: T) -> bool:
        current = self._root

        while current:
            if value < current.data:
                current = current.get_left()
            elif value > current.data:
                current = current.get_right()
            else:
                return True
        else:
            return False