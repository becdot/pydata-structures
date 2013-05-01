import unittest

from data_structures import Stack, Queue, Node, SinglyLinkedList, DoublyLinkedList, BinaryNode, BinaryTree
from data_structures import BinarySearchNode, HeapNode, Heap

def test_node(node, value, next, prev):
    return (node.value == value) and (node.next == next if node.next == None else node.next.value == next
        ) and (node.prev == prev if node.prev == None else node.prev.value == prev)

def test_linked_list(llist, head, tail):
    return (llist.head == head if llist.head == None else llist.head.value == head.value
        ) and (llist.tail == tail if llist.tail == None else llist.tail.value == tail.value)

def test_binary_node(node, value, left, right, parent):
        return (node.value == value) and (node.left == left if node.left == None else node.left.value == left
        ) and (node.right == right if node.right == None else node.right.value == right) and (
        node.parent == parent if node.parent == None else node.parent.value == parent)

def deep_btree():
    "Returns a root node filled in the below pattern"
    #               1
    #             /   \
    #           2       5
    #         /   \     /
    #       3       4   6
    #                  / \
    #                7    8

    node1 = BinaryNode(1)
    node2 = BinaryNode(2)
    node3 = BinaryNode(3)
    node4 = BinaryNode(4)
    node5 = BinaryNode(5)
    node6 = BinaryNode(6)
    node7 = BinaryNode(7)
    node8 = BinaryNode(8)
    node1.insert(node2)
    node1.insert(node5)
    node2.insert(node3)
    node2.insert(node4)
    node5.insert(node6)
    node6.insert(node7)
    node6.insert(node8)

    return node1

def wide_btree():
    "Returns a root node filled in the below pattern"
#               1
#             /   \
#           2       3
#         /   \     /
#       4       5   6
#                  / \
#                7    8
    
    node1 = BinaryNode(1)
    node2 = BinaryNode(2)
    node3 = BinaryNode(3)
    node4 = BinaryNode(4)
    node5 = BinaryNode(5)
    node6 = BinaryNode(6)
    node7 = BinaryNode(7)
    node8 = BinaryNode(8)
    node1.insert(node2)
    node1.insert(node3)
    node2.insert(node4)
    node2.insert(node5)
    node3.insert(node6)
    node6.insert(node7)
    node6.insert(node8)

    return node1

def binary_search_tree():
#               5
#             /    \
#           3        8
#         /  \     /
#       2     4   6
#      /           \
#     1             7

    node5 = BinarySearchNode(5)

    node5.insert(3)
    node5.insert(8)
    node5.insert(4)
    node5.insert(2)
    node5.insert(6)
    node5.insert(1)
    node5.insert(7)

    return node5

def max_heap():

#               17
#             /    \
#          15        10
#         /  \      /
#       6     10   7

    node17 = HeapNode(17)
    node15 = HeapNode(15)
    node10 = HeapNode(10)
    node6 = HeapNode(6)
    node10 = HeapNode(10)
    node7 = HeapNode(7)

    node17.left = node15
    node17.right = node10
    node15.parent, node10.parent = node17, node17
    node15.left = node6
    node15.right = HeapNode(10)
    node6.parent, node15.right.parent = node15, node15
    node10.left = node7
    node7.parent = node10
    return node17



class TestDataStructures(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(range(1, 6))
        self.queue = Queue(range(1, 6))
        self.single = SinglyLinkedList()
        self.double = DoublyLinkedList()
        self.btree = BinaryTree()

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

    # Binary Tree
    def test_binary_node_equality(self):
        one = BinaryNode(1)
        one2 = BinaryNode(1)
        self.assertTrue(one == one2)
        two = BinaryNode(2)
        self.assertFalse(one == two)

    def test_add_internal_child_to_binary_node(self):
        one = BinaryNode(1)
        two = BinaryNode(2)
        three = BinaryNode(3)
        one.left = three
        # one = {left: 3, right: None}
        one.insert(two, three)
        self.assertTrue(test_binary_node(one, 1, 2, None, None))
        self.assertTrue(test_binary_node(two, 2, 3, None, 1))
        self.assertTrue(test_binary_node(three, 3, None, None, 2))

    def test_add_external_child_to_binary_node(self):
        one = BinaryNode(1)
        two = BinaryNode(2)
        one.insert(two)
        self.assertTrue(test_binary_node(one, 1, 2, None, None))
        self.assertTrue(test_binary_node(two, 2, None, None, 1))
        three = BinaryNode(3)
        one.insert(three)
        self.assertTrue(test_binary_node(one, 1, 2, 3, None))
        self.assertTrue(test_binary_node(two, 2, None, None, 1))
        self.assertTrue(test_binary_node(three, 3, None, None, 1))
        four = BinaryNode(4)
        two.insert(four)
        self.assertTrue(test_binary_node(two, 2, 4, None, 1))
        self.assertTrue(test_binary_node(four, 4, None, None, 2))

    def test_depth_first_generation(self):
        self.btree.root = deep_btree()
        self.assertEquals([int(str(n)) for n in self.btree.depth_gen(self.btree.root)], range(1, 9))

    def test_breadth_first_generation(self):
        self.btree.root = wide_btree()
        self.assertEqual([int(str(n)) for n in self.btree.breadth_gen([self.btree.root])], range(1, 9))

    def test_binary_tree_iteration(self):
        self.btree.root = deep_btree()
        self.assertEquals([int(str(n)) for n in self.btree], range(1, 9))

    def test_contains(self):
        self.btree.root = deep_btree()
        for i in range(1, 9):
            self.assertTrue(i in self.btree)
        self.assertFalse(0 in self.btree)
        self.assertFalse(9 in self.btree)

    def test_insert_into_binary_tree(self):
        ## note - indexing grabs the node with that VALUE, not the node that exists at that index
        #       1
        self.btree.insert(1)
        self.assertTrue(test_binary_node(self.btree[1], 1, None, None, None))
        self.btree.insert(4, 1)
        #       1
        #      /
        #     4
        self.assertTrue(test_binary_node(self.btree[1], 1, 4, None, None))
        self.assertTrue(test_binary_node(self.btree[4], 4, None, None, 1))
        self.btree.insert(3, 1)
        #       1
        #      / \
        #     4   3
        self.assertTrue(test_binary_node(self.btree[1], 1, 4, 3, None))
        self.assertTrue(test_binary_node(self.btree[4], 4, None, None, 1))
        self.assertTrue(test_binary_node(self.btree[3], 3, None, None, 1))
        self.btree.insert(2, 1, 4)
        #       1
        #      / \
        #     2   3
        #    /
        #   4
        self.assertTrue(test_binary_node(self.btree[1], 1, 2, 3, None))
        self.assertTrue(test_binary_node(self.btree[2], 2, 4, None, 1))
        self.assertTrue(test_binary_node(self.btree[3], 3, None, None, 1))
        self.assertTrue(test_binary_node(self.btree[4], 4, None, None, 2))


    # Binary Search Tree
    def test_binary_search_node(self):
        root = binary_search_tree()
        for i in range(1, 9):
            self.assertTrue(root.search(i))
        self.assertFalse(root.search(0))
        self.assertFalse(root.search(9))

    def test_binary_search_insert(self):
    #               5
    #             /    \
    #           3        8
    #         /  \     /
    #       2     4   6

        root = BinarySearchNode(5)
        self.assertTrue(test_binary_node(root, 5, None, None, None))
        root.insert(3)
        self.assertTrue(test_binary_node(root, 5, 3, None, None))
        self.assertTrue(test_binary_node(root[3], 3, None, None, 5))
        root.insert(8)
        self.assertTrue(test_binary_node(root, 5, 3, 8, None))
        self.assertTrue(test_binary_node(root[3], 3, None, None, 5))
        self.assertTrue(test_binary_node(root[8], 8, None, None, 5))
        root.insert(4)
        self.assertTrue(test_binary_node(root, 5, 3, 8, None))
        self.assertTrue(test_binary_node(root[3], 3, None, 4, 5))
        self.assertTrue(test_binary_node(root[8], 8, None, None, 5))
        self.assertTrue(test_binary_node(root[4], 4, None, None, 3))
        root.insert(2)
        self.assertTrue(test_binary_node(root, 5, 3, 8, None))
        self.assertTrue(test_binary_node(root[3], 3, 2, 4, 5))
        self.assertTrue(test_binary_node(root[8], 8, None, None, 5))
        self.assertTrue(test_binary_node(root[2], 2, None, None, 3))
        self.assertTrue(test_binary_node(root[4], 4, None, None, 3))
        root.insert(6)
        self.assertTrue(test_binary_node(root, 5, 3, 8, None))
        self.assertTrue(test_binary_node(root[3], 3, 2, 4, 5))
        self.assertTrue(test_binary_node(root[8], 8, 6, None, 5))
        self.assertTrue(test_binary_node(root[2], 2, None, None, 3))
        self.assertTrue(test_binary_node(root[4], 4, None, None, 3))
        self.assertTrue(test_binary_node(root[6], 6, None, None, 8))

    # def test_binary_search_remove_external_node(self):
    #     root = binary_search_tree()
    #     root.remove(1)
    #     self.assertTrue(test_binary_node(root, 5, 3, 8, None))
    #     self.assertTrue(test_binary_node(root[3], 3, 2, 4, 5))
    #     self.assertTrue(test_binary_node(root[8], 8, 6, None, 5))
    #     self.assertTrue(test_binary_node(root[2], 2, None, None, 3))
    #     self.assertTrue(test_binary_node(root[4], 4, None, None, 3))
    #     self.assertTrue(test_binary_node(root[6], 6, None, 7, 8))
    #     self.assertTrue(test_binary_node(root[7], 7, None, None, 6))
    #     self.assertFalse(1 in root)
    #     self.assertFalse(root.search(1))

    def test_binary_search_remove_internal_node_without_children(self):
        root = binary_search_tree()
        root.remove(3, root[4])
        self.assertTrue(test_binary_node(root, 5, 4, 8, None))
        self.assertTrue(test_binary_node(root[4], 4, 2, None, 5))
        self.assertTrue(test_binary_node(root[8], 8, 6, None, 5))
        self.assertTrue(test_binary_node(root[2], 2, 1, None, 4))
        self.assertTrue(test_binary_node(root[6], 6, None, 7, 8))
        self.assertTrue(test_binary_node(root[7], 7, None, None, 6))
        self.assertFalse(3 in root)

    def test_binary_search_remove_internal_node_with_children1(self):
        root = binary_search_tree()
        root.insert(3.5)
        root.insert(4.5)
        root.remove(3, root[4])

        self.assertTrue(test_binary_node(root, 5, 4, 8, None))
        self.assertTrue(test_binary_node(root[4], 4, 3.5, 4.5, 5))
        self.assertTrue(test_binary_node(root[8], 8, 6, None, 5))
        self.assertTrue(test_binary_node(root[2], 2, 1, None, 3.5))
        self.assertTrue(test_binary_node(root[6], 6, None, 7, 8))
        self.assertTrue(test_binary_node(root[1], 1, None, None, 2))
        self.assertTrue(test_binary_node(root[3.5], 3.5, 2, None, 4))
        self.assertTrue(test_binary_node(root[4.5], 4.5, None, None, 4))
        self.assertTrue(test_binary_node(root[7], 7, None, None, 6))
        self.assertFalse(3 in root)

    def test_binary_search_remove_internal_node_with_children2(self):
        root = binary_search_tree()
        root.insert(3.5)
        root.insert(4.5)
        root.remove(3, root[2])

        self.assertTrue(test_binary_node(root, 5, 2, 8, None))
        self.assertTrue(test_binary_node(root[2], 2, 1, 4, 5))
        self.assertTrue(test_binary_node(root[8], 8, 6, None, 5))
        self.assertTrue(test_binary_node(root[6], 6, None, 7, 8))
        self.assertTrue(test_binary_node(root[1], 1, None, None, 2))
        self.assertTrue(test_binary_node(root[4], 4, 3.5, 4.5, 2))
        self.assertTrue(test_binary_node(root[3.5], 3.5, None, None, 4))
        self.assertTrue(test_binary_node(root[4.5], 4.5, None, None, 4))
        self.assertTrue(test_binary_node(root[7], 7, None, None, 6))
        self.assertFalse(3 in root)

    # HEAP
    def test_heap_iteration(self):
        heap = Heap(max_heap())
        self.assertEqual([int(str(n)) for n in heap.breadth()], [17, 15, 10, 6, 10, 7])
        self.assertEqual([int(str(n)) for n in heap], [17, 15, 10, 6, 10, 7])
        self.assertEqual(heap.flatten(), [17, 15, 10, 6, 10, 7])

    def test_find_open_with_empty_aunt(self):
        node17 = HeapNode(17)
        node15 = HeapNode(15)
        node11 = HeapNode(11)
        node6 = HeapNode(6)
        node10 = HeapNode(10)
        node17.left = node15
        node17.right = node11
        node15.left = node6
        node15.right = HeapNode(10)

        heap = Heap(node17)
        for node in heap:
            pass
        self.assertEqual(node.value, 10)
        self.assertEqual(heap.find_open(), (node11, 'left'))

    def test_find_open_with_single_child_aunt(self):
        node17 = HeapNode(17)
        node15 = HeapNode(15)
        node11 = HeapNode(11)
        node6 = HeapNode(6)
        node10 = HeapNode(10)
        node7 = HeapNode(7)
        node17.left = node15
        node17.right = node11
        node15.left = node6
        node15.right = HeapNode(10)
        node11.left = node7

        heap = Heap(node17)
        for node in heap:
            pass
        self.assertEqual(node.value, 7)
        self.assertEqual(heap.find_open(), (node11, 'right'))

    def test_find_open_with_non_empty_aunt(self):
        node17 = HeapNode(17)
        node15 = HeapNode(15)
        node11 = HeapNode(11)
        node6 = HeapNode(6)
        node10 = HeapNode(10)
        node7 = HeapNode(7)
        node5 = HeapNode(5)
        node17.left = node15
        node17.right = node11
        node15.left = node6
        node15.right = HeapNode(10)
        node11.left = node7
        node11.right = node5
        
        heap = Heap(node17)
        for node in heap:
            pass
        self.assertEqual(node.value, 5)
        self.assertEqual(heap.find_open(), (node6, 'left'))

    def test_insert(self):
        node17 = HeapNode(17)
        heap = Heap(node17)
        heap.insert(15)
        self.assertTrue(test_binary_node(heap.root, 17, 15, None, None))
        self.assertTrue(test_binary_node(heap.root.left, 15, None, None, 17))
        heap.insert(10)
        self.assertTrue(test_binary_node(heap.root, 17, 15, 10, None))
        self.assertTrue(test_binary_node(heap.root.left, 15, None, None, 17))        
        self.assertTrue(test_binary_node(heap.root.right, 10, None, None, 17))
        heap.insert(6)
        self.assertTrue(test_binary_node(heap.root, 17, 15, 10, None))
        self.assertTrue(test_binary_node(heap.root.left, 15, 6, None, 17))        
        self.assertTrue(test_binary_node(heap.root.right, 10, None, None, 17))
        self.assertTrue(test_binary_node(heap.root.left.left, 6, None, None, 15))
        heap.insert(10)
        self.assertTrue(test_binary_node(heap.root, 17, 15, 10, None))
        self.assertTrue(test_binary_node(heap.root.left, 15, 6, 10, 17))        
        self.assertTrue(test_binary_node(heap.root.right, 10, None, None, 17))
        self.assertTrue(test_binary_node(heap.root.left.left, 6, None, None, 15))
        self.assertTrue(test_binary_node(heap.root.left.right, 10, None, None, 15))
        heap.insert(7)
        self.assertTrue(test_binary_node(heap.root, 17, 15, 10, None))
        self.assertTrue(test_binary_node(heap.root.left, 15, 6, 10, 17))        
        self.assertTrue(test_binary_node(heap.root.right, 10, 7, None, 17))
        self.assertTrue(test_binary_node(heap.root.left.left, 6, None, None, 15))
        self.assertTrue(test_binary_node(heap.root.left.right, 10, None, None, 15))
        self.assertTrue(test_binary_node(heap.root.right.left, 7, None, None, 10))

    def test_percolate(self):

        #               17                      17                  100
        #             /    \                  /    \               /    \
        #          15        10    -->     15       100    -->   15       17
        #         /  \      /  \          /  \      /  \        /  \     /  \
        #       6     10   7   100      6     10   7   10     6     10  7   10

        heap = Heap(max_heap())
        parent = heap.root.right
        last = HeapNode(100)
        parent.right = last
        last.parent = parent
        heap.percolate(last)

        self.assertTrue(test_binary_node(heap.root, 100, 15, 17, None))
        self.assertTrue(test_binary_node(heap.root.right, 17, 7, 10, 100))
        self.assertTrue(test_binary_node(heap.root.right.left, 7, None, None, 17))
        self.assertTrue(test_binary_node(heap.root.right.right, 10, None, None, 17))

        #             100                  100                  100
        #            /    \               /    \               /    \
        #          15       17   -->    15       17    -->  99       17
        #         /  \     /  \        /  \     /  \        /  \     /  \
        #       6     10  7   10     99   10  7   10     15     10  7   10
        #      /                     /                   /
        #     99                   6                   6

        parent = heap.root.left.left
        last = HeapNode(99)
        last.parent = parent
        parent.left = last
        heap.percolate(last)
        self.assertTrue(test_binary_node(heap.root, 100, 99, 17, None))
        self.assertTrue(test_binary_node(heap.root.left, 99, 15, 10, 100))
        self.assertTrue(test_binary_node(heap.root.left.left, 15, 6, None, 99))
        self.assertTrue(test_binary_node(heap.root.left.right, 10, None, None, 99))
        self.assertTrue(test_binary_node(heap.root.left.left.left, 6, None, None, 15))

        #             100                  100                  100
        #            /    \               /    \               /    \
        #          99       17   -->    99       17    -->  100       17
        #         /  \     /  \        /  \     /  \        /  \      /  \
        #       15    10  7   10     15  100  7   10     15    99   7   10
        #      /  \   /             / \   /              /  \   /
        #     6   12 100          6  12 10             6   12 10

        fifteen = heap.root.left.left
        twelve = HeapNode(12)
        twelve.parent = fifteen
        fifteen.right = twelve

        ten = heap.root.left.right
        last = HeapNode(100)
        ten.left = last
        last.parent = ten
        heap.percolate(last)
        self.assertTrue(test_binary_node(heap.root, 100, 100, 17, None))
        self.assertTrue(test_binary_node(heap.root.left, 100, 15, 99, 100))
        self.assertTrue(test_binary_node(heap.root.left.left, 15, 6, 12, 100))
        self.assertTrue(test_binary_node(heap.root.left.right, 99, 10, None, 100))


    def test_insertion_with_percolation(self):
        #               17
        #             /    \
        #          15        10
        #         /  \      /
        #       6     10   7

        #     6
        six = HeapNode(6)
        heap = Heap(six)
        self.assertTrue(test_binary_node(heap.root, 6, None, None, None))

        #     6             10
        #    /    -->     /
        #  10           6
        heap.insert(10)
        self.assertTrue(test_binary_node(heap.root, 10, 6, None, None))
        self.assertTrue(test_binary_node(heap.root.left, 6, None, None, 10))          
        #     10             10
        #    /  \  -->     /   \
        #  6     7       6      7
        heap.insert(7)
        self.assertTrue(test_binary_node(heap.root, 10, 6, 7, None))
        self.assertTrue(test_binary_node(heap.root.left, 6, None, None, 10)) 
        self.assertTrue(test_binary_node(heap.root.right, 7, None, None, 10))
        #      10            15
        #     /  \  -->     /   \
        #   6     7       10      7
        #  /              / 
        # 15             6
        heap.insert(15)
        self.assertTrue(test_binary_node(heap.root, 15, 10, 7, None))
        self.assertTrue(test_binary_node(heap.root.left, 10, 6, None, 15)) 
        self.assertTrue(test_binary_node(heap.root.right, 7, None, None, 15))
        self.assertTrue(test_binary_node(heap.root.left.left, 6, None, None, 10))
        #      15            17
        #     /  \  -->     /   \
        #   10    7       15      7
        #  /  \          /  \
        # 6    17       6    10
        heap.insert(17)
        self.assertTrue(test_binary_node(heap.root, 17, 15, 7, None))
        self.assertTrue(test_binary_node(heap.root.left, 15, 6, 10, 17)) 
        self.assertTrue(test_binary_node(heap.root.right, 7, None, None, 17))
        self.assertTrue(test_binary_node(heap.root.left.left, 6, None, None, 15))
        self.assertTrue(test_binary_node(heap.root.left.right, 10, None, None, 15))
        #       17             17    
        #      /   \  -->     /   \   
        #    15     7       15     11
        #   /  \   /       /  \   /  
        #  6   10 11      6   10 7  
        heap.insert(11)
        self.assertTrue(test_binary_node(heap.root, 17, 15, 11, None))
        self.assertTrue(test_binary_node(heap.root.left, 15, 6, 10, 17)) 
        self.assertTrue(test_binary_node(heap.root.right, 11, 7, None, 17))
        self.assertTrue(test_binary_node(heap.root.left.left, 6, None, None, 15))
        self.assertTrue(test_binary_node(heap.root.left.right, 10, None, None, 15))
        self.assertTrue(test_binary_node(heap.root.right.left, 7, None, None, 11))









if __name__ == '__main__':
    unittest.main()