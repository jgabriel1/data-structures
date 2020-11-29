from binary_tree.main import BinaryTree
from unittest import TestCase


class TestBinaryTree(TestCase):
    def test_able_to_check_that_value_is_in(self):
        tree = BinaryTree()

        self.assertFalse(1 in tree)

    def test_inserting_values(self):
        tree = BinaryTree()

        tree.insert(5)
        tree.insert(6)
        tree.insert(7)

        self.assertIn(7, tree)
        self.assertIn(6, tree)
        self.assertIn(5, tree)
