"""
recurse for each element, keep track of visited element for each recursion level to avoid duplicates, backtrack/pop after returning the dfs
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        n = len(nums)
        result = []

        def dfs(path, visited):
            if len(path) == n:
                result.append(list(path))
                return
            for num in nums:
                if num not in visited:
                    path.append(num)
                    visited.add(num)
                    dfs(path, visited)
                    path.pop()
                    visited.remove(num)

        dfs([], set())
        return result
