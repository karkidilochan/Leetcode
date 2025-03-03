from typing import List

"""
for an efficient solution, we need to figure out the start of a sequence
i.e. a number whose num-1 is not in the set
build a hash set, and keep increasing length as you find num+length in the set
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                while (num + count) in nums_set:
                    count += 1
                max_count = max(max_count, count)
        return max_count
