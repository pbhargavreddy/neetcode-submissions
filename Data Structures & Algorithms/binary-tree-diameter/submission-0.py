# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Dfs
        max_diameter = 0
        # @classmethod
        def backtrack(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_height = backtrack(node.left)
            right_height = backtrack(node.right)
            max_diameter = max(max_diameter,left_height+right_height)
            return 1+max(left_height,right_height)
        backtrack(root)
        return max_diameter