from typing import List

"""
first check if midpoint lies in left half or right half
i.e. which side of the midpoint is sorted
if mid> end, left half is sorted
then find if target lies in the sorted half or other side
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] > nums[end]:
                # this means left half is sorted
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # nums[mid] <= nums[end]
                # this means right half is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
