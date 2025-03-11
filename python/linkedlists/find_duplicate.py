from typing import List

"""
brute force for O(1) space complexity: nested loops to check for same elements
O(1) space complexity: use a bitset, use or for every number, use and to check if bit at ith position is set
O(n) time complexity: cycle detection using floyd's tortoise and hare algorithm
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # floyd's tortoise and hare algorithm
        slow = nums[0]
        fast = nums[0]
        # cycle detection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                # cycle detected
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        # bit-set approach
        bitset = 0
        for num in nums:
            bits = 1 << num
            if bitset & bits:
                return num
            bitset |= bits
        return -1
