# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        visited = deque()

        if root: 
            visited.append(root)
        
        depth = 0 
        while visited: 

            
            for i in range(len(visited)): 
                node = visited.popleft()
                if node.left: 
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right) 

            depth+=1 

        return depth 