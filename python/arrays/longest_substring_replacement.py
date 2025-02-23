"""
Sliding window with two pointers:
right one moves, keeping track of frequency of each character, and the max_frequency found so far
if the len of current window - max_frequency > k, then we need to shrink the window, left moves towards right 
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        max_freq = 0
        max_len = 0
        from collections import defaultdict

        freq = defaultdict(int)
        for j in range(len(s)):
            freq[s[j]] += 1
            max_freq = max(max_freq, freq[s[j]])
            while ((j - i + 1) - max_freq) > k:
                freq[s[i]] -= 1
                i += 1
            max_len = max(max_len, j - i + 1)

        return max_len
