from typing import Generic, List, Optional, TypeVar

from queue.errors import QueueOverflowError, QueueUnderflowError

T = TypeVar("T")


class Queue(Generic[T]):

    _queue: List[T]
    _capacity: int

    def __init__(self, capacity: int) -> None:
        self._queue = []
        self._capacity = capacity

    def __len__(self) -> int:
        return len(self._queue)

    def __repr__(self) -> str:
        return f"Queue(IN {self._queue} OUT)"

    @property
    def is_full(self) -> bool:
        return len(self) == self._capacity

    @property
    def is_empty(self) -> bool:
        return len(self) == 0

    @property
    def front(self) -> Optional[T]:
        if not self.is_empty:
            return self._queue[-1]

    @property
    def rear(self) -> Optional[T]:
        if not self.is_empty:
            return self._queue[0]

    def enqueue(self, item: T) -> None:
        if self.is_full:
            raise QueueOverflowError

        self._queue.insert(0, item)

    def dequeue(self) -> T:
        if self.is_empty:
            raise QueueUnderflowError

        item = self._queue.pop()
        return item
