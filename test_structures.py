import unittest

from data_structures import Stack, Queue, Node, SinglyLinkedList

class TestDataStructures(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(range(1, 6))
        self.queue = Queue(range(1, 6))
        self.single = SinglyLinkedList()

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

# SINGLY-LINKED LIST
    def test_add_nodes_to_single(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        self.single.insert(node1)
        self.single.insert(node2, node1)
        self.assertEqual(self.single.head.value, 1)
        next = self.single.head.next
        self.assertEqual(next, node2)
        self.assertEqual(next.value, 2)
        self.single.insert(node3, node2)
        nextnext = self.single.head.next.next
        self.assertEqual(nextnext, node3)

    def test_add_node_to_beginning_of_single(self):
        node0, node1 = Node(0), Node(1)
        self.single.insert(node1)
        self.single.insert(node0)
        self.assertEqual(self.single.head.value, 0)
        self.assertEqual(self.single.head.next.value, 1)

    def test_remove_nodes_single(self):
        node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
        self.single.insert(node1)
        self.single.insert(node2, node1)
        self.single.insert(node3, node2)
        self.single.insert(node4, node3)
        self.single.remove(node2)
        self.assertEqual(node2.next, node4)

    def test_remove_node_from_beginning_single(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        self.single.insert(node1)
        self.single.insert(node2, node1)
        self.single.insert(node3, node2)
        self.single.remove()
        self.assertEqual(self.single.head, node2)

    def test_single_iteration(self):
        node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
        self.single.insert(node1)
        self.single.insert(node2, node1)
        self.single.insert(node3, node2)
        self.single.insert(node4, node3)
        self.assertEqual([node for node in self.single], [node1, node2, node3, node4])


if __name__ == '__main__':
    unittest.main()