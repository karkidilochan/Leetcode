"""
brute force: go through all substrings and check if they are palindromes: O(n^3)
two pointers: treat each character as a center and expand outwards, with odd and even approaches: O(n^2)

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0

        def expand_from_center(left, right):
            nonlocal s
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        result = ""
        for i in range(len(s)):
            # bab
            odd = expand_from_center(i, i)
            # bb
            even = expand_from_center(i, i + 1)
            result = max(odd, even, result, key=len)

        return result


"""
DP O(n^2) time and O(n^2) space: start from the end, keep 2d array updated for left,right, update result if palindrome and >max
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        max_len = 0
        result = ""
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    str_len = j - i + 1
                    if str_len <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if str_len > max_len and dp[i][j]:
                        result = s[i : j + 1]
                        max_len = str_len

        return result
