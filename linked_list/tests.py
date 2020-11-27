from linked_list.main import LinkedList
from unittest import TestCase


class TestLinkedList(TestCase):
    def test_access_item(self):
        linked_list = LinkedList("first", "second", "third")

        first = linked_list[0]
        second = linked_list[1]
        third = linked_list[2]

        self.assertEquals(first, "first")
        self.assertEquals(second, "second")
        self.assertEquals(third, "third")

    def test_able_to_iterate_over(self):
        linked_list = LinkedList(1, 2, 3)

        for item in linked_list:
            self.assertIn(item, {1, 2, 3})

    def test_add_item_to_end(self):
        linked_list = LinkedList[str]("first", "second")

        linked_list.add_to_end("third")
        last_element = linked_list[-1]

        self.assertEquals(last_element, "third")

    def test_add_item_to_start(self):
        linked_list = LinkedList[int](1, 2, 3)

        linked_list.add_to_start(0)
        first_item = linked_list[0]

        self.assertEquals(first_item, 0)
