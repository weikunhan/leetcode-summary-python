# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.res = False
        
        if not root:
            self.res = True
            
            return self.res
        
        self.res = self.dfs(root.left, root.right)
            
        return self.res
        
    def dfs(self, root_left, root_right):
        if not root_left or not root_right:
            if root_left == root_right:
                
                return True
            else:
                return False
            
        if root_left.val == root_right.val and self.dfs(root_left.left, root_right.right) and self.dfs(root_left.right, root_right.left):
            
            return True
        
        return False