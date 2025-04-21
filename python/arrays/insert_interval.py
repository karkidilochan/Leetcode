# Linear Search Approach: Time Complexity O(n), Space Complexity O(1)
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        new_intervals = []
        i = 0

        # case1: find intervals to skip
        while i < n and newInterval[0] > intervals[i][1]:
            new_intervals.append(intervals[i])
            i += 1

        # case2: overlap
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        new_intervals.append(newInterval)

        # no need to assimilate anymore
        while i < n:
            new_intervals.append(intervals[i])
            i += 1
        return new_intervals


# Binary Search Approach: Time Complexity O(log n), Space Complexity O(1)
# binary search optimization performed on linear search approach
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        new_intervals = []
        i = 0

        # first find the insertion point
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if newInterval[0] > intervals[mid][0]:
                left = mid + 1
            else:
                right = mid - 1
        intervals.insert(left, newInterval)

        # now adjust ranges while inserting to the new array
        for interval in intervals:
            # if new array is empty, simply insert the first element
            if not new_intervals:
                new_intervals.append(interval)
            elif new_intervals[-1][1] < interval[0]:
                new_intervals.append(interval)
            else:
                # fix the range
                new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
        return new_intervals
