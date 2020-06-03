# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        self.res = False
        
        self.res = self.dfs(s, t)
        
        return self.res
    
    def dfs(self, root_s, root_t):
        if self.helper(root_s, root_t):
            
            return True
        
        if not root_s:
            
            return False
        
        if self.dfs(root_s.left, root_t) or self.dfs(root_s.right, root_t):
            
            return True
        
        return False
        
    def helper(self, root_s, root_t):
        if not root_s or not root_t:
            if root_s == root_t:
                
                return True
            else:
                
                return False
            
        if root_s.val ==root_t.val and self.helper(root_s.left, root_t.left) and self.helper(root_s.right, root_t.right):
            
            return True
        
        return False