from typing import Any, Generic, Iterator, NewType, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):

    data: T
    _next: Optional["Node"]

    def __init__(self, data: T) -> None:
        self.data = data
        self._next = None

    def __repr__(self) -> str:
        return f"Node({self.data}, {self._next})"

    def set_next(self, node: "Node" = None):
        self._next = node

    def get_next(self) -> Optional["Node"]:
        return self._next


class LinkedList(Generic[T]):

    _head: Optional[Node]

    def __init__(self, *items: T) -> None:
        iterator = iter(items)
        self._head = self._build_linked_list(iterator)

    def __repr__(self) -> str:
        return [item for item in self].__repr__()

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __iter__(self) -> Iterator[T]:
        head = self._head

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
        _position = len(self) + position if position < 0 else position

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

    def _set_head(self, new_head: Optional[Node]) -> None:
        self._head = new_head

    def _extend_node(self, node: Node) -> None:
        if self._head is None:
            self._set_head(node)
        else:
            self._head.set_next(node)

    def contains(self, data: T) -> bool:
        for item in self:
            if item == data:
                return True
        else:
            return False

    def add_to_start(self, data: T) -> None:
        new_head = Node(data)
        new_head.set_next(self._head)

        self._head = new_head

    def add_to_end(self, data: T) -> None:
        """
        The time complexity has to be O(N), since the entire list needs to be iterated
        through to get to the last node.
        """
        current = self._head

        # When the list is empty, adding to start has the same effect:
        if current is None:
            return self.add_to_start(data)

        while current.get_next():
            current = current.get_next()

        new_head = Node(data)

        current.set_next(new_head)

    def insert(self, index: int, data: T) -> None:
        """
        Insert an item in a specific position of the list. Time complexity is O(index).
        The algorithm has to iterate over the list all the way up to the point where the
        new item will be added.
        """

        current = self._head

        if index == 0:
            return self.add_to_start(data)

        for i, _ in enumerate(self):
            if i + 1 == index:
                rest = current.get_next()

                new_node = Node(data)
                new_node.set_next(rest)

                current.set_next(new_node)

                break

            current = current.get_next()
        else:
            raise IndexError("Cannot insert to index out of range.")

    def pop(self) -> T:
        """
        Remove the last item of the list returning it.
        """
        current = self._head

        if current is None:
            raise IndexError("Cannot pop from empty list")

        while True:
            next_node = current.get_next()

            if next_node.get_next() is None:
                item = next_node.data

                current.set_next(None)

                return item

            current = current.get_next()

    def remove(self, index: int) -> T:
        """
        Remove an item from the list at a specific index.
        """
        buffer = LinkedList()
        head = self._head

        for i, item in enumerate(self):
            if i == index:
                buffer._extend_node(head.get_next())
                self._set_head(buffer._head)

                return item

            buffer.add_to_end(item)
            head = head.get_next()
        else:
            raise IndexError