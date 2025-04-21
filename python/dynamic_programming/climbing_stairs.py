"""
Think of climbing stairs as a tree structure. At each step, you can either take 1 step or 2 steps, creating two nodes for each step.
Use dfs to explore all possible paths from the root (step 0) to the leaf nodes (step n).
"""


# Recursive Approach with DFS
class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(i):
            nonlocal n
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                return dfs(i + 1) + dfs(i + 2)

        result = dfs(1) + dfs(2)
        return result


"""
Dynamic Programming Approach - Top-Down with Memoization
1. Create a memoization dictionary to store computed values
"""


class Solution:

    def climbStairs(self, n: int) -> int:

        def dfs(i, precomputed={}):
            nonlocal n
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                if i not in precomputed:
                    precomputed[i] = dfs(i + 1, precomputed) + dfs(i + 2, precomputed)
                return precomputed[i]

        result = dfs(1) + dfs(2)
        return result


"""
Dynamic Programming Approach - Bottom-Up with Tabulation
1. Create a tabulation array to store computed values starting from 3rd step to nth step
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        table = [0] * (n + 1)
        table[1], table[2] = 1, 2

        for i in range(3, n + 1):
            table[i] = table[i - 1] + table[i - 2]

        return table[n]
