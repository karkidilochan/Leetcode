"""
for each element, either include it in subset or not,
gives series of actions for 2^n subsets
for n elements
backtracking: popping recently added element
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        subset = []

        def run(i):
            if i >= len(nums):
                powerset.append(subset.copy())
                return
            num = nums[i]
            subset.append(num)
            run(i + 1)
            subset.pop()
            run(i + 1)

        run(0)
        return powerset
