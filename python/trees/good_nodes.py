"""
keep track of max in dfs and count when max is updated, start with the root value
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return root

        count_good_nodes = 0

        def dfs(node, max_value):
            nonlocal count_good_nodes

            if node.val >= max_value:
                max_value = max(node.val, max_value)
                count_good_nodes += 1

            if node.left:
                dfs(node.left, max_value)
            if node.right:
                dfs(node.right, max_value)

        dfs(root, root.val)

        return count_good_nodes
