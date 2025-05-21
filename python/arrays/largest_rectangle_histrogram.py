class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = 0
        max_area = float("-inf")
        min_height = float("inf")

        for i in range(len(heights)):
            min_height = min(min_height, heights[i])
            cum_area = (i - left + 1) * min_height
            print(heights[i], min_height, cum_area, max_area)
            if cum_area < heights[i]:
                left = i
                cum_area = heights[i]
                min_height = heights[i]
            max_area = max(cum_area, max_area)
        return max_area
