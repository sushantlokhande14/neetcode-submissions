# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return None 

        leftMax = maxDepth(root.left)
        rightMax = maxDepth(root.right)

        depth = max(leftMax, rightMax)
        
        return 1+ depth