# similar to walls and gates leetcode problem

"""
my solution uses dfs, starting from the 0s, and traversing to next node if its inf or 
the distance is less than the current distance -> time complexity is O(m×n×4 pow(m×n))

optimal solution is use bfs, starting from inf, add neighboring lands to queue if not visited
iterate through the queue at each level and return if treasure found, with the accumulated steps
"""
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 0:
                    self.dfs(i, j, 0)

    def dfs(self, i, j, distance):
        if distance <= self.grid[i][j]:
            self.grid[i][j] = distance

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni
                    and ni < len(self.grid)
                    and 0 <= nj
                    and nj < len(self.grid[0])
                ):
                    self.dfs(ni, nj, distance + 1)
