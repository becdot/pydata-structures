import unittest

from data_structures import Stack, Queue

class TestDataStructures(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(range(1, 6))
        self.queue = Queue(range(1, 6))
        self.single = SinglyLinkedList()
        self.double = DoublyLinkedList()

    # STACK
    def test_stack_push(self):
        self.stack.push(6)
        self.assertEqual(self.stack.stack, range(1, 7)) 

    def test_stack_pop(self):
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.pop(), 4)

    def test_stack_peek(self):
        self.assertEqual(self.stack.peek(), 5)

    # QUEUE
    def test_queue_push(self):
        self.queue.push(6)
        self.assertEqual(self.queue.queue, range(1, 7))

    def test_queue_pop(self):
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)

    def test_queue_peek(self):
        self.assertEqual(self.queue.peek(), 1)
        self.queue.pop()
        self.assertEqual(self.queue.peek(), 2)



if __name__ == '__main__':
    unittest.main()