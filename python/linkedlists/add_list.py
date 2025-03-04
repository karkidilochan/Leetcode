from typing import Optional

"""
loop through list while one of the nodes exists or carry over is not 0
put modulus of sum to the new list node and carry over to the next node
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curra = l1
        currb = l2
        currc = newhead = None
        carry = 0
        while curra or currb:
            a = curra.val if curra else 0
            b = currb.val if currb else 0
            sum = a + b + carry
            c = (sum) % 10
            carry = (sum) // 10
            if not newhead:
                newhead = currc = ListNode(c)
            else:
                currc.next = ListNode(c)
                currc = currc.next
            curra = curra.next if curra else None
            currb = currb.next if currb else None
        if carry != 0:
            currc.next = ListNode(carry)
        return newhead
