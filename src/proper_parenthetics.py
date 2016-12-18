"""
This module implements a doubly linked list and checks for values.

We want to make sure every open parenthesis has a closing one.
If there is an unmatched open paren, the function will return 1.
If there is an unmatched closed paren, it will return -1.
If all parens are matched in the doubly linked list, it returns 0.
"""


class Node():
    """Instantiate a node."""

    def __init__(self, value=None, nxt=None, previous=None):
        """."""
        self.value = value
        self.next = nxt
        self.previous = previous


class Queue():
    """Instantiate a doubly linked list."""

    def __init__(self, iter=None):
        """."""
        self.head = None
        self.tail = None
        self.length = 0
        if iter and hasattr(iter, "__iter__"):
            for item in iter:
                self.push(item)
        elif iter:
            raise TypeError

    def push(self, value=None):
        """Push value to the head of dll."""
        new_node = Node(value, nxt=self.head)
        if self.length < 1:
            self.tail = new_node
        else:
            self.head.previous = new_node
        self.head = new_node
        self.length += 1

    def is_balanced(self):
        """Check for the number and place of parenthesis."""
        counter = 0
        curr = self.tail
        while curr:
            if curr.value == "(":
                counter += 1
            elif curr.value == ")":
                counter -= 1
            if counter < 0:
                return -1
            curr = curr.previous
        if counter > 0:
            return 1
        if counter == 0:
            return counter
