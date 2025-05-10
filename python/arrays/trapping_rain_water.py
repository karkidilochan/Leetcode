"""
water at each point is min(leftmax, rightmax) - height
two passes to find leftmax and rightmax for each point
for 2p, use left,right pointers to find leftmax and rightmax
update the smallest of leftmax and rightmax with +1 and find unit by subtracting
height from the smallest of leftmax and rightmax
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[0], height[n - 1]
        total = 0
        while left < right:
            # unit = min(leftmax, rightmax)-height
            # unit = smallest among leftmax, rightmax - height?
            if left_max < right_max:
                left_max = max(left_max, height[left + 1])
                total += left_max - height[left + 1]
                left += 1
            else:
                right_max = max(right_max, height[right - 1])
                total += right_max - height[right - 1]
                right -= 1

        return total
