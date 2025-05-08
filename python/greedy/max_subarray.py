"""
kadane's algorithm: discard previous sum if it is less than current number
O(n) time complexity, O(1) space complexity
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]

        for num in nums[1:]:
            # don't keep previous sum if it is less than current number
            curr_sum = max(curr_sum + num, num)
            max_sum = max(curr_sum, max_sum)

        return max_sum


"""
DP solution:

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        table = [0] * n
        max_sum = float("-inf")

        for i in range(n):
            table[i] = max(table[i - 1] + nums[i], table[i])
            max_sum = max(table[i], max_sum)
        return max_sum


"""
brute force with memoization: O(n^2) time complexity, O(1) space complexity
loop through each element and sum all elements from i to j

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        table = [[0] * n for _ in range(n)]
        max_sum = float("-inf")

        for i in range(n):
            table[i][i] = nums[i]
            max_sum = max(nums[i], max_sum)
        print(table)

        for i in range(n):
            for j in range(i + 1, n):
                table[i][j] = table[i][j - 1] + nums[j]
                max_sum = max(max_sum, table[i][j])
                print(table)
        return max_sum
