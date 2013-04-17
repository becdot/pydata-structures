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
    "Node with pointer/s and value"

    def __init__(self, value):
        self.value = value
        self.next = None

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
    
    def insert(self, node, previous=None):
        if previous:
            node.next = previous.next
            previous.next = node
        else:
            node.next = self.head
            self.head = node

    def remove(self, previous=None):
        if previous:
            previous.next = previous.next.next if previous.next else None
        else:
            self.head = self.head.next

