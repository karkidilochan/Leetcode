"""
in the subsets with unique elements problem, just add while loop to skip duplicates
time: O(n*2^n), space: O(n)
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)
        nums.sort()

        def backtrack(i):
            if i >= n:
                result.append(path[:])
                return
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
            # skip duplicates
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return result
