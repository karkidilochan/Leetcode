"""
condition to merge intervals: start<=last_end and end>=last_start,
sort the intervals to get a sequence of ascending intervals
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        for start, end in intervals:

            if result and start <= result[-1][1] and end >= result[-1][0]:
                result[-1] = [min(start, result[-1][0]), max(end, result[-1][1])]

            else:
                result.append([start, end])

        return result
