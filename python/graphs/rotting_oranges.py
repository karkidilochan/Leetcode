from collections import deque
from typing import List

"""
go through the grid and find all the rotten oranges and add them to the queue
then run bfs on the queue, keeping track of the current level
update fresh to rotten, and at the end check if fresh count is zero.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.grid = grid
        self.queue = deque()
        self.fresh = 0
        result = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if grid[i][j] == 2:
                    self.queue.appendleft((i, j))
                elif grid[i][j] == 1:
                    self.fresh += 1
        if self.queue:
            result = self.bfs()
        if self.fresh == 0:
            return result
        else:
            return -1
        return result

    def bfs(self):
        run = -1
        while self.queue:
            run += 1
            size = len(self.queue)
            for _ in range(size):
                i, j = self.queue.pop()
                if self.grid[i][j] == 1:
                    self.grid[i][j] += 1
                    self.fresh -= 1
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if (
                        ni >= 0
                        and ni < len(self.grid)
                        and nj >= 0
                        and nj < len(self.grid[0])
                        and not (ni, nj) in self.visited
                        and self.grid[ni][nj] == 1
                    ):
                        self.queue.appendleft((ni, nj))
                        self.visited.add((ni, nj))
        return run
