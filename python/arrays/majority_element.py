"""
O(n), O(n) solution
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import defaultdict

        n_map = defaultdict(int)

        for num in nums:
            n_map[num] += 1
            if n_map[num] > (n / 2):
                return num


"""
boyer-Moore Voting Algorithm
the majority element's count remain when subtracted by counts of all other elements
O(n), O(1) solution
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        candidate = None
        curr_count = 0

        for num in nums:
            if curr_count == 0:
                candidate = num
            if candidate == num:
                curr_count += 1
            else:
                curr_count -= 1
        return candidate
