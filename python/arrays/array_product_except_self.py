# for O(n) solution:
# first pass: calculate the prefix product shifted to right by one
# second pass: calculate the suffix product shifted to left by one


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prod = 1
        for i in range(0, len(nums)):
            output[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]

        return output
