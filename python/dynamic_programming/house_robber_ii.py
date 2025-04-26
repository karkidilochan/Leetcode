"""run dp for two instances:
1. if first element taken, slice out last element,
2. if second element taken iterate until last element"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 4:
            return max(nums)

        prev1, prev2 = 0, 0
        for num in nums[:-1]:
            curr = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = curr

        first_result = prev2

        prev1, prev2 = 0, 0
        for num in nums[1:]:
            curr = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = curr
        second_result = prev2

        return max(first_result, second_result)
