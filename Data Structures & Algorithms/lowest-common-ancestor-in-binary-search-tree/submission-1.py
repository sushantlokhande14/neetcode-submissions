# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root: 
            if p <= root.val and q <= root.val: 
                lowestCommonAncestor(root.left)
            elif p >= root.val and q>=root.val: 
                lowestCommonAncestor(root.right)
            elif p <= root.val  and q >= root.val: 
                return root.val

        return None