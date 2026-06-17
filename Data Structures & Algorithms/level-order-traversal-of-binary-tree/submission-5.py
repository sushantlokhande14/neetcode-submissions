# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            curr = [] 
            level_size = len(queue)
            for i in range(level_size): 
                node = queue.popleft()
                curr.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(curr)

        return res




