"""
Iterative 2P: O(n^2) => expand around center to count odd and even length palindromes
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0

        # O(n)
        def expand_center(left, right):
            nonlocal substrings
            while left >= 0 and right < len(s) and s[left] == s[right]:
                substrings += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_center(i, i)

            expand_center(i, i + 1)

        return substrings


"""
Dynamic Programming: O(n^2) => substring is palindrome if substring i+1, j-1 is palindrome
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # i,j is palindrome if i+1, j-1 is palindrome
        n = len(s)
        table = [[False] * n for _ in range(n)]
        palindromes = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                sub_len = j - i + 1
                if s[i] == s[j]:
                    if sub_len <= 2 or table[i + 1][j - 1]:
                        table[i][j] = True
                        palindromes += 1

        return palindromes
