import random
import math

class Stack(object):
    """First-in, last-out data structure.
        Elements can be pushed onto or popped off the stack; can also peek at the top element."""
    # error handling?
    # implementation with a linked list?
    
    def __init__(self, array):
        self.stack = array

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

# Queue
class Queue(object):
    """First-in, first-out data structure.
        Elements can be pushed onto the end of the queue, and popped off the front of the queue."""
    # error handling?
    # implementation with a singly- or doubly-linked list?

    def __init__(self, array):
        self.queue = array

    def push(self, elem):
        self.queue.append(elem)

    def pop(self):
        elem = self.queue[0]
        self.queue = self.queue[1:]
        return elem

    def peek(self):
        return self.queue[0]

# Singly-linked list
class Node(object):
    "Node with pointer/s and value -- self.prev used only for doubly-linked list"

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class SinglyLinkedList(object):
    """Collection of nodes, each with a value and a pointer to the next node.
        Nodes can be inserted and removed after existing nodes."""

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        return str([str(node) for node in self])

    def __getitem__(self, index):
        for i, item in enumerate(self):
            if i == index:
                return item
        else:
            raise IndexError

    def __len__(self):
        return sum(1 for i in self)
    
    def insert(self, value, index):
        if index == 0:
            self._insert(Node(value))
            return
        for i, n in enumerate(self): 
            if i == index:
                self._insert(Node(value), n)
                break
        else:
            self._insert(Node(value), n)

    def _insert(self, node, previous=None):
        if previous:
            node.next = previous.next
            previous.next = node
        else:
            node.next = self.head
            self.head = node

    def remove(self, index):
        if index == 0:
            self._remove()
            return
        for i, n in enumerate(self):
            if i == index - 1:
                self._remove(n)
                break
        else:
            raise IndexError, "list assignment index out of range"

    def _remove(self, previous=None):
        if previous:
            previous.next = previous.next.next if previous.next else None
        else:
            self.head = self.head.next

# Doubly-linked list
class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return sum(1 for node in self)

    def __str__(self):
        return str([str(node) for node in self])

    def __getitem__(self, index):
        for i, n in enumerate(self):
            if i == index:
                return n
        else:
            raise IndexError

    def insert(self, value, index):
        """Inserts Node(value) at the index -- iterates forward if index is in the first half of the list
            and backwards if index is in the second half of the list"""
        # to insert at the beginning, or when the list is empty
        if not(len(self) and index):
            self._insert(Node(value))
        # to insert at the end of a list
        elif index >= len(self):
            self._rev_insert(Node(value))
        # iterate forwards
        elif len(self)/2.0 > index:
            # iterate forwards
            for i, n in enumerate(self):
                if i == index:
                    self._insert(Node(value), n)
        # iterate backwards
        else:
            for i, n in enumerate(reversed(self)):
                if abs(i - len(self) + 1) == index:
                    self._rev_insert(Node(value), n)
                    break

    def _insert(self, node, prev_node=None):
        """Inserts node after prev_node -- base implementation of insert().  
            If prev_node is not provided, inserts at the beginning"""
        self.tail = node if self.tail == prev_node else self.tail
        if prev_node:
            node.next = prev_node.next
            node.prev = prev_node
            prev_node.next = node
            if node.next:
                node.next.prev = node
        else:
            if self.head: 
                self.head.prev = node
            node.next = self.head
            self.head = node

    def _rev_insert(self, node, prev_node=None):
        """Inserts node after prev_node, moving in reverse.
           e.g given a list [A, C], insert(B, C) -> [A, B, C]
            If prev_node is not provided, inserts at the end of the list"""
        self.head = node if self.head == prev_node else self.head
        if prev_node:
            node.prev = prev_node.prev
            node.next = prev_node
            prev_node.prev = node
            if node.prev:
                node.prev.next = node
        else:
            if self.tail:
                self.tail.next = node
            node.prev = self.tail
            self.tail = node


# Binary Tree
## UNSORTED
class BinaryNode(object):
    # always inserts to the left

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value if isinstance(other, BinaryNode) else False

    def __ne__(self):
        return self.value != other.value if isinstance(other, BinaryNode) else True 

    @property
    def empty(self):
        return not(self.right or self.left) 

    def insert(self, node, child=None):
        if child and (child.left or child.right):
            raise AttributeError("Node cannot have any children.")
        # we want to insert the node internally
        if child:
            direction = 'left' if self.left == child else 'right'
            node.left = getattr(self, direction)
            node.parent = self
            child.parent = node
            setattr(self, direction, node)
        # we want to add the node externally
        else:
            # add node to self.left if self.left is currently unassigned
            self.left = self.left if self.left else node
            # add node to self.right if self.right is unassigned and you haven't just assigned self.left
            self.right = self.right if self.right or self.left == node else node
            node.parent = self

    # def depth(self):
    #     yield self
    #     if self.left:
    #         for node in self.left.depth():
    #             yield node
    #     if self.right:
    #         for node in self.right.depth():
    #             yield node


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def __iter__(self):
        "Iterates depthwise through the tree"
        for node in self.depth_gen(self.root):
            yield node

    def __contains__(self, value):
        "Returns True if value exists in the tree, else returns False"
        for node in self:
            if node.value == value:
                return True
        return False

    def __getitem__(self, value):
        "Value is the value of the node, NOT the index"
        for node in self:
            if node.value == value:
                return node

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self):
        return self.value != other.value


    def depth_gen(self, node):
        "Generates nodes moving depthwise"
        if node.empty:
            yield node
        else:
            yield node
            if node.left:
                left = self.depth_gen(node.left)
                for n in left:
                    yield n
            if node.right:
                right = self.depth_gen(node.right)
                for n in right:
                    yield n

    def breadth_gen(self, node_list):
        "Just for fun -- semi-lazy implementation"
        next = []
        for node in node_list:
            yield node
            next.append(node.left) if node.left else None
            next.append(node.right) if node.right else None
        if next:
            for n in self.breadth_gen(next):
                yield n

    def insert(self, value, parent_value=None, child_value=None):
        """Inserts the value between the parent node and the child node
            If child node does not exist, tries to add the node as a leaf to the parent"""
        new_node = BinaryNode(value)
        child_node = self[child_value] if child_value else None
        if parent_value:
            for node in self:
                if node.value == parent_value:
                    node.insert(new_node, child_node)
        else:
            self.root = BinaryNode(value)

# Binary Search Tree
class BinarySearchNode(BinaryNode):
    
    def __contains__(self, value):
        if self.search(value):
            return True
        return False

    def __getitem__(self, value):
        node = self.search(value)
        if node:
            return node
        else:
            raise AttributeError("{} does not exist".format(value))

    def search(self, value):
        "Traverses the tree -- average time of log(n)"
        if self.value == value:
            return self
        elif value > self.value:
            return self.right.search(value) if self.right else None
        else:
            return self.left.search(value) if self.left else None

    def insert(self, value):
        "Inserts a node with value in the appropriate place.  Cannot have duplicate nodes."
        if self.value == value:
            raise IndexError("{} already exists".format(value))
        elif self.right and value > self.value:
            return self.right.insert(value)
        elif self.left and value < self.value:
            return self.left.insert(value)
        elif value > self.value:
            self.right = BinarySearchNode(value)
            self.right.parent = self
        else:
            self.left = BinarySearchNode(value)
            self.left.parent = self

    def _delete(self, successor=None):
        "Delete node by updating its parent and child/ren -- should not be called directly"
        # successor is only used for testing purposes, to prevent the successor from being chosen randomly
        if not(self.left and self.right):
            # if node has one or fewer children, deletion is easy
            # update parent to point to our child, if it exists
            self.parent.left = self.left if self.parent.left == self else self.parent.left
            self.parent.right = self.right if self.parent.right == self else self.parent.right
            # update our child, if it exists, to point to our parent
            if self.left:
                self.left.parent = self.parent
            if self.right:
                self.right.parent = self.parent
        else:
            # if node has two children, have to choose which child replaces it
            successor = successor or random.choice([self.left, self.right])
            # update parent to point to successor
            successor.parent = self.parent
            successor.parent.left = successor if successor.parent.left == self else successor.parent.left
            successor.parent.right = successor if successor.parent.right == self else successor.parent.right
            # move our children to be children of successor (or of successor's children)
            if successor == self.right:
                ext_left = successor
                while ext_left.left:
                    ext_left = ext_left.left
                ext_left.left = self.left
                self.left.parent = ext_left
            else:
                ext_right = successor
                while ext_right.right:
                    ext_right = ext_right.right
                ext_right.right = self.right
                self.right.parent = ext_right
        del self

    def remove(self, value, successor=None):
        "Removes the node with value. Successor is for testing purposes, since delete chooses the successor randomly"
        if self.value == value:
            self._delete(successor)
        elif self.right and value >= self.value:
            return self.right.remove(value, successor)
        elif self.left and value <= self.value:
            return self.left.remove(value, successor)
        else:
            raise AttributeError("{} does not exist".format(value))


# Heap
class HeapNode(BinaryNode):
    pass    
    # can have duplicates in a heap
    # def __eq__(self, other):
    #     return self == other

    # def __ne__(self, other):
    #     return self == other

    # @staticmethod
    # def breadth(children):
    #     next = []
    #     for node in children:
    #         yield node
    #         next.append(node.left) if node.left else None
    #         next.append(node.right) if node.right else None
    #     if next:
    #         for n in Heap.breadth(next):
    #             yield n

    # def depth(self, level=0):
    #     "Generator that yields (value, level) where root level = 0, root child level = 1, etc"
    #     yield self.value, level
    #     level = level if self.empty else level + 1
    #     if self.left:
    #         for node in self.left.depth(level):
    #             yield node
    #     if self.right:
    #         for node in self.right.depth(level):
    #             yield node



            
class Heap(object):

    def __init__(self, root=None, array=None):
        if array:
            self.build_from_array(array)

        else:
            self.root = root
            self.last = [n for n in self][-1]

    def __iter__(self):
        for node in self.breadth():
            yield node

    def flatten(self):
        return [int(str(n)) for n in self]

    def breadth(self, children=None):
        children = [self.root] if children == None else children
        next = []
        for node in children:
            yield node
            next.append(node.left) if node.left else None
            next.append(node.right) if node.right else None
        if next:
            for n in self.breadth(next):
                yield n

    def find_last(self):
        for node in self:
            if node.right:
                continue
            elif node.left:
                return (node, 'right')
            else:
                return (node, 'left')


    def insert(self, value):
        node = HeapNode(value)
        parent, place = self.find_last()
        node.parent = parent
        setattr(parent, place, node)


# (Hash table, Trie)