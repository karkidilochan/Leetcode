"""
BFS; while traversing queue, use for loop to pop all elements at the same level
go through each element treating them as right, at the end of the loop you get the right side



DFS: dfs while keeping track of the level, call dfs on the right first, then left
at each recurrence, if its the first time we see the level, add it to the result => len(result) == level
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque, defaultdict

        queue = deque([(root, 0)])
        levels = defaultdict(list)
        while queue:
            curr, level = queue.popleft()
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
            levels[level].append(curr.val)
        result = [values[-1] for key, values in levels.items()]
        return result
