# get character count of p first, can use an array of 26
# then slide a window of length of p over s, and update the counts of character, remove character counts if length exceeds that of p


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        from collections import defaultdict

        p_len = len(p)

        p_map = defaultdict(int)
        for c in p:
            p_map[c] += 1

        result = []
        s_map = defaultdict(int)

        for i in range(len(s)):
            s_map[s[i]] += 1

            if sum(s_map.values()) > p_len:
                s_map[s[i - p_len]] -= 1
                if s_map[s[i - p_len]] == 0:
                    del s_map[s[i - p_len]]

            if s_map == p_map:
                result.append(i - p_len + 1)

        return result
