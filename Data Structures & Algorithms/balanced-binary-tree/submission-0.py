# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: 
                return True, 0 

            leftBalanced , left = dfs(node.left)
            rightBalanced , right = dfs(node.right)

            currbalanced = (leftBalanced and rightBalanced and abs(left - right) <= 1)
            
            currheight = l + max(left,right)

            return currbalanced, currheight 
        
        bal , h = dfs(root) 

        return bal

            