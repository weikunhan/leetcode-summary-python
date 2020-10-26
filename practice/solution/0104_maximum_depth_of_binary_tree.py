# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        
        self.res = self.dfs(root)
        
        return self.res
    
    def dfs(self, root):
        temp_value = 0
        
        if not root:
            
            return temp_value
        
        temp_value = 1 + max(self.dfs(root.left), self.dfs(root.right))
        
        return temp_value