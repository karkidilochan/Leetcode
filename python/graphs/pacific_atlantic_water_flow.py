from typing import List

"""
traversing the grid and starting dfs/bfs from each cell would make the recursion depth too large
instead, start from the edges of pacific and atlantic and dfs/bfs from there to cells with larger
heights. 
keep track of separate visited cells in pacific and atlantic and return intersection
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])

        self.heights = heights
        self.visited_a = set()
        result = []

        self.visited_p = set()
        for i in range(self.m):
            self.dfs(i, 0, self.visited_p)
            self.dfs(i, self.n - 1, self.visited_a)
        for j in range(self.n):
            self.dfs(0, j, self.visited_p)
            self.dfs(self.m - 1, j, self.visited_a)

        for i in range(self.m):
            for j in range(self.n):
                if (i, j) in self.visited_p and (i, j) in self.visited_a:
                    result.append([i, j])
        return result

    def dfs(self, i, j, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if (
                ni >= 0
                and ni < self.m
                and nj >= 0
                and nj < self.n
                and self.heights[ni][nj] >= self.heights[i][j]
            ):
                self.dfs(ni, nj, visited)
