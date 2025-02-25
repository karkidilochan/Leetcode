from typing import List, Optional
from collections import deque, defaultdict

"""
bfs, for each node, add its children and current level + 1 to the queue,
 and use hashmap to keep track of node values at each level
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = defaultdict(list)
        result = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.pop()
            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))
            levels[level].append(node.val)

        for key, value in levels.items():
            result.append(value)
        return result
