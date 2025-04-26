"""build counters for both strings, and compare them
keep a running counter and sliding window of len(s1) so you don't have to build the counter
for every substring of len(s1)
for running counter, if len exceeds required length, decrease/remove the leftmost element

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        ohmap = defaultdict(int)
        for c in s1:
            ohmap[c] += 1

        left = 0
        thmap = defaultdict(int)
        for right in range(0, len(s2)):
            thmap[s2[right]] += 1

            if right - left + 1 > len(s1):
                thmap[s2[left]] -= 1
                if thmap[s2[left]] == 0:
                    del thmap[s2[left]]
                left += 1

            if ohmap == thmap:
                return True
        return False
