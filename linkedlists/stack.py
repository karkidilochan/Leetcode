from typing import Optional


class Node:
    def __init__(self, value, previous=None) -> None:
        self.value = value
        self.previous: Optional[Node] = previous


class Stack:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def push(self, item):
        new_node = Node(item)

        if not self.head:
            self.head = new_node
            self.length += 1
            return

        new_node.previous = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        old_head = self.head
        self.head = self.head.previous
        self.length = max(0, self.length - 1)
        return old_head

    def peek(self):
        return self.head.value
