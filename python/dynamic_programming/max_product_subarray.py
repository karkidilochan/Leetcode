"""
keep track of negative numbers as well, record the max and min at each iteration,
update max_product with max of max_product, min product and max at each iteration
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        table = [0] * n
        table[0] = (nums[0], nums[0])
        max_product = max(float("-inf"), nums[0])
        for i in range(1, n):
            nmin, nmax = table[i - 1]
            table[i] = (
                max(nmin * nums[i], nmax * nums[i], nums[i]),
                min(nmax * nums[i], nmin * nums[i], nums[i]),
            )

            max_product = max(table[i][0], max_product)
        return max_product
