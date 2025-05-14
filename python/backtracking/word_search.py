"""
go through each cell, compare the letter with the each subsequent letter in the word,
if match, look in the other directions, with a visited set to avoid going back
increment index of word while recursing,
remember: mutable objects are passed by reference, so remove the cell from visited set when backtracking
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(row, col, pointer, visited):
            if board[row][col] == word[pointer]:
                visited.add((row, col))

                if pointer == len(word) - 1:
                    return True
                for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    nrow, ncol = row + di, col + dj
                    if (
                        0 <= nrow < rows
                        and 0 <= ncol < cols
                        and (nrow, ncol) not in visited
                        and backtrack(nrow, ncol, pointer + 1, visited)
                    ):
                        return True
                visited.remove((row, col))
            return False

        visited = set()
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0, visited):
                    return True

        return False
