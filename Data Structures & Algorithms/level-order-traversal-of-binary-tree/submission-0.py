# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque([])
        queue.append(root)
        while len(queue)!=0:
            level_size = len(queue)
            sub_res = []
            for _ in range(level_size):
                e = queue.popleft()
                sub_res.append(e.val)
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
            result.append(sub_res)
        return result
