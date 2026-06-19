# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root): 
        res = []
        self.traverse(root.left)
        res.append(root.val)
        self.traverse(root.right)

        return res 






    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root: 
            res = self.traverse(root)
            return res[k]
        else: 
            return []