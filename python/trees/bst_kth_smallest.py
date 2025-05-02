"""
inorder traversal of bst gives sorted elements, can keep a decreasing counter after left dfs for more efficient solution
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def dfs(node):
            nonlocal result
            if not node:
                return node
            left = dfs(node.left)
            if left:
                result.append(left.val)
            result.append(node.val)
            right = dfs(node.right)
            if right:
                result.append(right.val)

        dfs(root)
        return result[k - 1]
