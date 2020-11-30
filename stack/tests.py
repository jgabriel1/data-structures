from unittest import TestCase

from stack.errors import StackOverflowError, StackUnderflowError
from stack.main import Stack


class TestStack(TestCase):
    def test_is_empty_prop(self):
        stack = Stack()

        self.assertTrue(stack.is_empty)

    def test_is_full_prop(self):
        stack = Stack(size=2)

        stack.push(True)
        stack.push(True)

        self.assertTrue(stack.is_full)

    def test_push_adds_item(self):
        stack = Stack()

        stack.push("item")

        self.assertFalse(stack.is_empty)

    def test_pop_removes_item_returning_it(self):
        stack = Stack()

        stack.push("item")

        item = stack.pop()

        self.assertTrue(stack.is_empty)
        self.assertEquals(item, "item")

    def test_peek_does_not_alter_stack(self):
        stack = Stack()

        stack.push("item")

        item = stack.peek()

        self.assertEquals(item, "item")
        self.assertTrue(len(stack), 1)

    def test_last_in_first_out(self):
        stack = Stack()

        stack.push("first in")
        stack.push("second in")

        first_out = stack.pop()
        second_out = stack.pop()

        self.assertEquals(first_out, "second in")
        self.assertEquals(second_out, "first in")

    def test_raises_on_stack_overflow(self):
        stack = Stack(size=1)

        stack.push("first")

        push_second_item = lambda: stack.push("second")

        self.assertRaises(StackOverflowError, push_second_item)

    def test_raises_on_empty_stack_popping(self):
        stack = Stack()

        pop_item = lambda: stack.pop()

        self.assertRaises(StackUnderflowError, pop_item)
