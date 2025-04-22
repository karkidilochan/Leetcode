# BFS Approach: use the topological sort approach, start with the 0s, then traverse the queue for cells whose
# results haven't been computed yet, increment by 1 for each of them


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        from collections import deque

        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rows, cols = len(mat), len(mat[0])
        result_mat = [[-1] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                visited_node = set()
                if mat[i][j] == 0:
                    result_mat[i][j] = 0
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and result_mat[ni][nj] == -1:
                    result_mat[ni][nj] = result_mat[i][j] + 1
                    queue.append((ni, nj))

        return result_mat


"""
Dynamic Programming Approach:
need to use results from neighboring cells to calculate the result for the current cell
but, not sure if neighboring cells have been computed yet
so, we do two passes, one from top to bottom, and one from bottom to top
1. Create a result matrix of the same size as the input matrix, initialized with -1.
2. Traverse the input matrix from top to bottom, and for each cell, check its neighboring cells (up, left) to calculate the result.
3. Traverse the input matrix from bottom to top, and for each cell, check its neighboring cells (down, right) to calculate the result.

"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        result_mat = [[float("inf")] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result_mat[i][j] = 0
                else:
                    if i > 0:
                        result_mat[i][j] = min(
                            result_mat[i][j], result_mat[i - 1][j] + 1
                        )
                    if j > 0:
                        result_mat[i][j] = min(
                            result_mat[i][j], result_mat[i][j - 1] + 1
                        )

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i < rows - 1:
                    result_mat[i][j] = min(result_mat[i][j], result_mat[i + 1][j] + 1)
                if j < cols - 1:
                    result_mat[i][j] = min(result_mat[i][j], result_mat[i][j + 1] + 1)

        return result_mat
