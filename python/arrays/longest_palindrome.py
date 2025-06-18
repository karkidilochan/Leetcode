# find the odd count and subtract from length, add one before returning


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict

        s_map = defaultdict(int)
        pal_count = 0
        for c in s:
            s_map[c] += 1

            if s_map[c] % 2 == 0:
                pal_count += 2

        if pal_count < len(s):
            pal_count += 1

        return pal_count
