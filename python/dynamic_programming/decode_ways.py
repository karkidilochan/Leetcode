"""
build decision tree, if end reached return 1 else 0, accumulate the counts
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        table = [0] * len(s)

        def dfs(idx, precomputed={}):
            if idx in precomputed:
                return precomputed[idx]
            if idx > len(s):
                return 0
            if idx == len(s):
                return 1
            if s[idx] == "0":
                return 0
            total = 0

            total += dfs(idx + 1)
            if 10 <= int(s[idx : idx + 2]) <= 26:
                total += dfs(idx + 2)
            precomputed[idx] = total
            return total

        total = dfs(0)
        return total


"""
bottom up approach: one char: i= sum of i-1, two char: sum of i-2 since you take two characters, accumulate on no of ways from two characters back
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        table = [0] * (n + 1)
        if s[0] == "0":
            return 0
        table[0], table[1] = 1, 1
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                table[i] += table[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                table[i] += table[i - 2]
        return table[n]
