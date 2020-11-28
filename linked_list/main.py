from typing import Any, Generic, Iterator, NewType, Optional, TypeVar

T = TypeVar("T")

NodeType = NewType(name="NodeType", tp=Any)


class Node(Generic[T]):

    data: T
    _next: Optional[NodeType]

    def __init__(self, data: T) -> None:
        self.data = data
        self._next = None

    def __repr__(self) -> str:
        return f"Node({self.data}, {self._next})"

    def set_next(self, node: NodeType):
        self._next = node

    def get_next(self) -> NodeType:
        return self._next


class LinkedList(Generic[T]):

    _iterator: Iterator[T]
    _node: Optional[Node]

    def __init__(self, *items: T) -> None:
        iterator = iter(items)
        self._node = self._build_linked_list(iterator)

    def __repr__(self) -> str:
        return [item for item in self].__repr__()

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __iter__(self) -> Iterator[T]:
        head = self._node

        while True:
            try:
                # The last item of the list points to a None. Trying to access the property
                # data of None should raise an AttributeError.
                yield head.data

                head = head.get_next()
            except AttributeError:
                break

    def __getitem__(self, position: int) -> T:
        """
        O(K) where K is the index passed. The list has to be iterated to reach the index.
        TODO: Make this algorithm better for negative indexes. `len(self)` is expensive.
        """
        if position < 0:
            _position = len(self) + position
        else:
            _position = position

        for index, item in enumerate(self):
            if index == _position:
                return item
        else:
            raise IndexError

    def __contains__(self, data: T) -> bool:
        return self.contains(data)

    def _build_linked_list(self, iterator: Iterator[T]) -> Optional[Node]:
        try:
            item = next(iterator)
        except StopIteration:
            return None

        node = Node(item)
        node.set_next(self._build_linked_list(iterator))

        return node

    def contains(self, data: T) -> bool:
        for item in self:
            if item == data:
                return True
        else:
            return False

    def add_to_start(self, data: T) -> None:
        new_head = Node(data)
        new_head.set_next(self._node)

        self._node = new_head

    def add_to_end(self, data: T) -> None:
        """
        The time complexity has to be O(N), since the entire list needs to be iterated
        through to get to the last node.
        """
        current_head = self._node

        # When the list is empty, adding to start has the same effect:
        if current_head is None:
            return self.add_to_start(data)

        while current_head.get_next():
            current_head = current_head.get_next()

        new_head = Node(data)
        current_head.set_next(new_head)

        self._node = current_head

    def insert(self, index: int, data: T) -> None:
        """
        TODO: Insert an item in a specific position of the list.
        """
        ...

    def pop(self) -> T:
        """
        TODO: Remove the last item of the list returning it.
        """
        ...

    def remove(self, index: int) -> T:
        """
        TODO: Remove an item from the list at a specific index.
        """
        ...