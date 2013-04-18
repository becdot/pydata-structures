import unittest

from data_structures import Stack, Queue, Node, SinglyLinkedList, DoublyLinkedList

def test_node(node, value, next, prev):
    return (node.value == value) and (node.next == next if node.next == None else node.next.value == next
        ) and (node.prev == prev if node.prev == None else node.prev.value == prev)

def test_linked_list(llist, head, tail):
    return (llist.head == head if llist.head == None else llist.head.value == head.value
        ) and (llist.tail == tail if llist.tail == None else llist.tail.value == tail.value)

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

    # SINGLY-LINKED LIST
    def test_add_nodes_to_single(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        self.single._insert(node1)
        self.single._insert(node2, node1)
        self.assertEqual(self.single.head.value, 1)
        next = self.single.head.next
        self.assertEqual(next, node2)
        self.assertEqual(next.value, 2)
        self.single._insert(node3, node2)
        nextnext = self.single.head.next.next
        self.assertEqual(nextnext, node3)

    def test_add_node_to_beginning_of_single(self):
        node0, node1 = Node(0), Node(1)
        self.single._insert(node1)
        self.single._insert(node0)
        self.assertEqual(self.single.head.value, 0)
        self.assertEqual(self.single.head.next.value, 1)

    def test_remove_nodes_single(self):
        node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
        self.single._insert(node1)
        self.single._insert(node2, node1)
        self.single._insert(node3, node2)
        self.single._insert(node4, node3)
        self.single._remove(node2)
        self.assertEqual(node2.next, node4)

    def test_remove_node_from_beginning_single(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        self.single._insert(node1)
        self.single._insert(node2, node1)
        self.single._insert(node3, node2)
        self.single._remove()
        self.assertEqual(self.single.head, node2)

    def test_single_iteration(self):
        node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
        self.single._insert(node1)
        self.single._insert(node2, node1)
        self.single._insert(node3, node2)
        self.single._insert(node4, node3)
        self.assertEqual([node for node in self.single], [node1, node2, node3, node4])

    def test_add_node_to_single_for_real(self):
        self.single.insert(2, 0)
        self.assertEqual(self.single[0].value, 2)
        self.single.insert(1, 0)
        self.assertEqual(self.single[0].value, 1)
        self.single.insert(3, 2)
        self.assertEqual(self.single[2].value, 3)
        self.single.insert(4, 100)
        self.assertEqual(self.single[3].value, 4)

    def test_remove_node_from_single_for_real(self):
        for i in range(4, 0, -1):
            self.single.insert(i, 0)
        # [1, 2, 3, 4]
        self.single.remove(1)
        # [1, 3, 4]
        self.assertEqual(self.single[1].value, 3)
        self.single.remove(2)
        # [1, 3]
        self.assertEqual(self.single[0].value, 1)
        self.assertEqual(self.single[1].value, 3)

   # DOUBLE-LINKED LIST
    def test_iteration_double(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        node1.next, node2.next, node3.next = node2, node3, None
        node1.prev, node2.prev, node3.prev = None, node1, node2
        self.double.head = node1
        self.double.tail = node3
        # test __iter__
        self.assertEqual([str(i) for i in self.double], [str(i) for i in range(1, 4)])
        # test iterating over reversed
        self.assertEqual([str(i) for i in reversed(self.double)], [str(i) for i in range(3, 0, -1)])

    def test_double_slicing(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        node1.next, node2.next, node3.next = node2, node3, None
        node1.prev, node2.prev, node3.prev = None, node1, node2
        self.double.head = node1
        self.double.tail = node3
        self.assertEqual(self.double[0].value, 1)
        self.assertEqual(self.double[1].value, 2)
        self.assertEqual(self.double[2].value, 3)
        self.assertRaises(IndexError, lambda val: self.double[val], 3)

    def test_base_insert_moving_forwards_with_double(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        self.double._insert(node1)
        self.assertTrue(test_node(self.double[0], 1, None, None))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[0]))

        self.double._insert(node3, node1)
        self.assertTrue(test_node(self.double[0], 1, 3, None))
        self.assertTrue(test_node(self.double[1], 3, None, 1))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[1]))

        self.double._insert(node2, node1)
        self.assertTrue(test_node(self.double[0], 1, 2, None))
        self.assertTrue(test_node(self.double[1], 2, 3, 1))
        self.assertTrue(test_node(self.double[2], 3, None, 2))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[2]))

        self.assertEqual(str(self.double), str([str(i) for i in range(1, 4)]))

    def test_base_insert_moving_backwards_with_double(self):
        node1, node2, node3 = Node(1), Node(2), Node(3)
        # insert node3 at the beginning/end of the list
        self.double._rev_insert(node3)
        self.assertTrue(test_node(self.double[0], 3, None, None))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[0]))
        # insert node one before node 3 ([node1, node3])
        self.double._rev_insert(node1, node3)
        self.assertTrue(test_node(self.double[0], 1, 3, None))
        self.assertTrue(test_node(self.double[1], 3, None, 1))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[1]))
        # insert node2 before node3 ([node1, node2, node3])
        self.double._rev_insert(node2, node3)
        self.assertTrue(test_node(self.double[0], 1, 2, None))
        self.assertTrue(test_node(self.double[1], 2, 3, 1))
        self.assertTrue(test_node(self.double[2], 3, None, 2))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[2]))
        # check that the array is [node1, node2, node3]
        self.assertEqual(str(self.double), str([str(i) for i in range(1, 4)]))

    def test_insert_at_beginning_of_double(self):
        self.double.insert(2, 0)
        self.assertTrue(test_node(self.double[0], 2, None, None))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[0]))
        self.double.insert(1, 0)
        self.assertTrue(test_node(self.double[0], 1, 2, None))
        self.assertTrue(test_node(self.double[1], 2, None, 1))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[1]))

    def test_insert_in_middle_and_end_of_double(self):
        self.double.insert(1, 0)
        self.double.insert(3, 1)
        self.assertTrue(test_node(self.double[0], 1, 3, None))
        self.assertTrue(test_node(self.double[1], 3, None, 1))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[1]))
        self.double.insert(2, 1) 
        self.assertTrue(test_node(self.double[0], 1, 2, None))
        self.assertTrue(test_node(self.double[1], 2, 3, 1))
        self.assertTrue(test_node(self.double[2], 3, None, 2))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[2]))
        self.double.insert(5, 3) 
        self.assertTrue(test_node(self.double[0], 1, 2, None))
        self.assertTrue(test_node(self.double[1], 2, 3, 1))
        self.assertTrue(test_node(self.double[2], 3, 5, 2))
        self.assertTrue(test_node(self.double[3], 5, None, 3))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[3]))
        self.double.insert(4, 3) 
        self.assertTrue(test_node(self.double[0], 1, 2, None))
        self.assertTrue(test_node(self.double[1], 2, 3, 1))
        self.assertTrue(test_node(self.double[2], 3, 4, 2))
        self.assertTrue(test_node(self.double[3], 4, 5, 3))
        self.assertTrue(test_node(self.double[4], 5, None, 4))
        self.assertTrue(test_linked_list(self.double, self.double[0], self.double[4]))


if __name__ == '__main__':
    unittest.main()