# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height_cal(root):
            if root is None:
                return 0
            left = height_cal(root.left)
            if left == -1:
                return -1
            right = height_cal(root.right)
            if right == -1:
                return -1
            if abs(right-left)>1:
                return -1
            return 1 + max(left, right)
        
        x=height_cal(root)
        if x == -1:
            return False
        return True

        