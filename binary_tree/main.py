from typing import Generic, Optional, TypeVar

from binary_tree.types import Comparable

T = TypeVar("T", bound=Comparable)


class Node(Generic[T]):

    key: T
    _left: Optional["Node[T]"]
    _right: Optional["Node[T]"]

    def __init__(self, key: T) -> None:
        self.key = key
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
            if value < current.key:
                if current.get_left() is None:
                    current.set_left(Node(value))
                    break
                else:
                    current = current.get_left()
            elif value > current.key:
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
            if value < current.key:
                current = current.get_left()
            elif value > current.key:
                current = current.get_right()
            else:
                return True
        else:
            return False
