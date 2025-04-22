class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # a xor a  = 0
        # a xor 0 = a
        for num in nums:
            result ^= num
        return result
