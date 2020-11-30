from typing import Generic, Iterable, List, Optional, TypeVar

from stack.errors import NotIterableError, StackOverflowError, StackUnderflowError

T = TypeVar("T")


class Stack(Generic[T]):

    _stack: List[T]
    _size: Optional[int]

    def __init__(self, size: Optional[int] = None) -> None:
        self._stack = []
        self._size = size

    def __len__(self) -> int:
        return len(self._stack)

    def __iter__(self) -> None:
        raise NotIterableError

    def __repr__(self) -> str:
        return f"Stack({self._stack} TOP)"

    @property
    def is_empty(self) -> bool:
        return len(self) == 0

    @property
    def is_full(self) -> bool:
        has_size = self._size is not None

        if not has_size:
            return False

        return len(self) == self._size

    def push(self, item: T) -> None:
        if self.is_full:
            raise StackOverflowError

        self._stack.append(item)

    def pop(self) -> Optional[T]:
        if self.is_empty:
            raise StackUnderflowError

        return self._stack.pop()

    def peek(self) -> Optional[T]:
        if self.is_empty:
            return None

        return self._stack[-1]

    @classmethod
    def from_iterable(cls, iterable: Iterable[T]) -> "Stack[T]":
        stack = cls()
        stack._stack = list(iterable)

        return stack
