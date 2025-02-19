from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # with dfs
        visited = set()

        def dfs(i, j):
            nonlocal grid

            # if already visited this node, no need to count again
            if (i, j) in visited:
                return 0

            # starting from a land, look around in all four directions
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1

            visited.add((i, j))

            return dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        # first search for land
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    # start depth search from this node
                    return dfs(i, j)

        return 0
