# Go through entire array to understand the subproblems
# At each elements, we can either take 1 step or 2 steps back, if 1 one step back, don't add current value, if 2 steps back, add current value
# at each sub problem, we can memoize the previous results, -> DP


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        if len(nums) < 2:
            return nums[-1]

        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            rob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = rob

        return rob2
