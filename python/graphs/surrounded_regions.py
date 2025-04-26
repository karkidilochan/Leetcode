"""
since we are excluding edges from modification, start search from edges, and populate with something else
then another loop to capture the rest, turn populated ones to the original value
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def bfs(i, j):
            nonlocal board, rows, cols

        from collections import deque

        queue = deque(())

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (
                    (i == 0 or i == rows - 1) or (j == 0 or j == cols - 1)
                ):
                    queue.append((i, j))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            i, j = queue.popleft()
            board[i][j] = "#"
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni <= rows - 1 and 0 <= nj <= cols - 1 and board[ni][nj] == "O":
                    queue.append((ni, nj))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
