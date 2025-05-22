class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index = 0
        for num in nums2:
            while index < len(nums1) and nums1[index] < num:
                index += 1
            nums1.insert(index, num)
        n = len(nums1)
        if n % 2:
            median = nums1[(n - 1) // 2]

        else:
            median = (nums1[n // 2 - 1] + nums1[n // 2]) / 2

        return median
