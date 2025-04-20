# check for original color after popping queue, since node in queue may be already changed
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        from collections import deque

        queue = deque([(sr, sc)])
        original_color = image[sr][sc]
        if original_color == color:
            return image
        while queue:
            i, j = queue.pop()
            if image[i][j] == original_color:
                image[i][j] = color
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for di, dj in directions:
                    ni = di + i
                    nj = dj + j
                    if (
                        (0 <= ni < len(image))
                        and (0 <= nj < len(image[0]))
                        and image[ni][nj] == original_color
                    ):
                        queue.appendleft((ni, nj))
        return image
