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