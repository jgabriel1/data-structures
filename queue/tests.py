from unittest import TestCase

from queue.errors import QueueOverflowError, QueueUnderflowError
from queue.main import Queue


class TestQueue(TestCase):
    def test_front_and_rear_props(self):
        queue = Queue(3)

        for number in [0, 1, 2]:
            queue.enqueue(number)

        self.assertEquals(queue.front, 0)
        self.assertEquals(queue.rear, 2)

    def test_first_in_first_out(self):
        queue = Queue(2)

        queue.enqueue("first in")
        queue.enqueue("last in")

        first_out = queue.dequeue()
        last_out = queue.dequeue()

        self.assertEquals("first in", first_out)
        self.assertEquals("last in", last_out)

    def test_raises_on_queue_overflow(self):
        queue = Queue(1)

        queue.enqueue("first")

        self.assertRaises(QueueOverflowError, lambda: queue.enqueue("second"))

    def test_raises_on_queue_underflow(self):
        queue = Queue(10)

        self.assertRaises(QueueUnderflowError, lambda: queue.dequeue())
