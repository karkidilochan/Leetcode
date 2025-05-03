"""
brute force: for each node in preorder, split the inorder into two halves and recurse
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # each dfs should return a root
        collection = []

        def dfs(sub_inorder, pre_index):
            if not sub_inorder or pre_index >= len(preorder):
                return None
            if preorder[pre_index] in sub_inorder:
                in_index = sub_inorder.index(preorder[pre_index])
                curr = TreeNode(preorder[pre_index])
                curr.left = dfs(sub_inorder[:in_index], pre_index + 1)
                curr.right = dfs(sub_inorder[in_index + 1 :], pre_index + 1)
                return curr
            else:
                return dfs(sub_inorder, pre_index + 1)

        return dfs(inorder, 0)


"""
hashmap to store inorder indexes, use left and right pointers for slices of splits based on index of preorder value
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # each dfs should return a root
        collection = []
        pre_index = 0
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def dfs(left, right):
            nonlocal pre_index

            if left > right:
                return None

            curr = TreeNode(preorder[pre_index])
            pointer = inorder_map[preorder[pre_index]]
            pre_index += 1

            curr.left = dfs(left, pointer - 1)
            curr.right = dfs(pointer + 1, right)

            return curr

        return dfs(0, len(inorder) - 1)
