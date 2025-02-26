from typing import Optional

"""
my approach is two pass: first recursion to copy the linkedlist, then second pas to update the random pointers
can be done in single pass: assign random pointer in the recursion function after the recursive call to node.next
this is a O(n) time and space complexity solution
for O(1) space complexity, interleave the list: node => new_node, creating a list where each node's next is its copy
then assign random pointers as curr.next.random = curr.random.next
then separate the two lists: copy_list = curr.next, curr.next = curr.next.next
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        def copy(node):
            nonlocal idx
            if not node:
                return node
            new_node = Node(node.val)
            new_node.next = copy(node.next)
            if node not in idx:
                idx[node] = new_node
            return new_node

        if not head:
            return head
        idx = {}
        new_head = copy(head)

        curr = head
        new_curr = new_head
        while curr and new_curr:
            if curr.random:
                new_curr.random = idx[curr.random]
            curr = curr.next
            new_curr = new_curr.next
        return new_head
