# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isvalid(self, root, min_val= float('-inf'), max_val= float('inf')):
        if root: 
            if min_val < root.val < max_val:
                return self.isvalid(root.left, min_val ,root.val) and self.isvalid(root.right, root.val, max_val )
            else: 
                return False
        return True  


    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        if root: 
            return self.isvalid(root)


        else: 
            return True