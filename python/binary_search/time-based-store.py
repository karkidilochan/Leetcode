"""
searching in the list of timestamps can be done in O(logn) time using binary search
store every midpoint timestamp <= given timestamp, if midpoint > given timestamp, shorten the right boundary
"""


class TimeMap:

    def __init__(self):
        from collections import defaultdict

        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([timestamp, value])

    """
    brute-force approach
        def get(self, key: str, timestamp: int) -> str:
        timestamps = self.hmap[key].keys()
        while timestamp not in timestamps:
            timestamp-=1
            if timestamp<=0:
                return ""
        return self.hmap[key][timestamp]
    """

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        timestamps = self.hmap[key]
        l, r = 0, len(timestamps) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if timestamps[mid][0] <= timestamp:
                res = timestamps[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
