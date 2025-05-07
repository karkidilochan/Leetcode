"""
keep count of each color, loop through nums for each count and update
O(n) time complexity, O(1) space complexity
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_map = {
            0: 0,
            1: 0,
            2: 0,
        }
        for n in nums:
            n_map[n] += 1
        result = []
        i = 0
        for key, value in n_map.items():
            print(key, value)
            while value > 0:
                nums[i] = key
                value -= 1
                i += 1


"""
TODO: in-place solution using edgers dijkstra
"""
