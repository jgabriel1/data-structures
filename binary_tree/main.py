from typing import Generic, Optional, TypeVar

T = TypeVar("T")


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
