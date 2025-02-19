from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = set()
        islands = 0
        for i in range(0, m):
            for j in range(0, n):
                if self.grid[i][j] == "1" and not ((i, j) in self.visited):
                    self.bfs(i, j)
                    islands += 1

        return islands

    def bfs(self, i, j):
        from collections import deque

        queue = deque([(i, j)])
        self.visited.add((i, j))
        while queue:
            i, j = queue.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
                    if self.grid[ni][nj] == "1" and (ni, nj) not in self.visited:
                        self.visited.add((ni, nj))
                        queue.append((ni, nj))
