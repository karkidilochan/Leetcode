"""
start from first character, word break valid only if starting with first,
loop through slices of string, if slice in word dict, recurse from that index
if end reached, return true
memoize the results for quick lookup
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)

        def dfs(i, memo={}):
            if i not in memo:
                if i == len(s):
                    memo[i] = True
                else:
                    memo[i] = False
                    for j in range(i, len(s)):
                        if s[i : j + 1] in word_dict:
                            if dfs(j + 1):
                                memo[i] = True

            return memo[i]

        return dfs(0)
