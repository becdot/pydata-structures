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

    def add_child(self, node, child=None):
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
            self.left = None if self.left else node
            # add node to self.right if self.right is unassigned and you haven't just assigned self.left
            self.right = None if self.right or self.left == node else node
            node.parent = self

class BinaryTree(object):

    def __init__(self):
        self.root = None

    def __iter__(self):
        pass

# Heap

# (Hash table, Trie)