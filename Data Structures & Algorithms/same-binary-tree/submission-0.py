# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if q.val!=p.val:
            return False

        left1 = self.isSameTree(p.left, q.left)
        
        right1 = self.isSameTree(p.right, q.right)

        return left1 and right1
