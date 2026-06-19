# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
class Solution:
    def traverse(self, root, res): 
        if root: 
            self.traverse(root.left, res )
            res.append(root.val)
            self.traverse(root.right, res)

        return


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root: 
            res = []
            self.traverse(root, res)
            return res[k-1]
        else: 
            return []

"""


class Solution: 
    def traverse_optimised(self, root, k, res = [] ): 
        counter = 0
        if root and counter <= k :

            self.traverse_optimised(root.left, k , res)
            res.append(root.val)
            counter+=1 
            self.traverse_optimised(root.right, k, res)
        
        return res[k-1]
     
            

    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if root: 
            return self.traverse_optimised(root, k ,  res )
