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

    def test_add_item_to_end_of_empty_list(self):
        linked_list = LinkedList()

        linked_list.add_to_end("item")

        self.assertIn("item", linked_list)

    def test_add_item_to_start(self):
        linked_list = LinkedList[int](1, 2, 3)

        linked_list.add_to_start(0)
        first_item = linked_list[0]

        self.assertEquals(first_item, 0)

    def test_add_item_to_start_of_empty_list(self):
        linked_list = LinkedList()

        linked_list.add_to_start("item")

        self.assertIn("item", linked_list)

    def test_insert_item_at_specific_index(self):
        linked_list = LinkedList[str]("apple", "banana", "cantaloupe")

        linked_list.insert(1, "mango")

        self.assertIn("mango", linked_list)
        self.assertEquals(linked_list[1], "mango")

    def test_pop_last_item_and_return_it(self):
        linked_list = LinkedList[str]("apple", "banana", "cantaloupe")

        cantaloupe = linked_list.pop()

        self.assertEquals(cantaloupe, "cantaloupe")
        self.assertNotIn("cantaloupe", linked_list)

    def test_not_able_to_pop_empty_list(self):
        linked_list = LinkedList()

        pop_from_empty_list = lambda: linked_list.pop()

        self.assertRaises(IndexError, pop_from_empty_list)

    def test_removes_item_in_specific_index(self):
        linked_list = LinkedList[str]("apple", "banana", "cantaloupe")

        banana = linked_list.remove(1)

        self.assertEquals(banana, "banana")
        self.assertNotIn("banana", linked_list)
