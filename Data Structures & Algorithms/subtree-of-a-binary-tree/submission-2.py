# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def __init__(self):
        self.res = 10
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def isSame(self,p,q):
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False
        left = self.isSame(p.left,q.left)
        right = self.isSame(p.right,q.right)
        return left and right and p.val == q.val