# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.res = False
        
        self.res = self.dfs(root, root.val)
        
        return self.res
        
    def dfs(self, root, target):
        if not root:
            
            return True
        
        if root.val == target and self.dfs(root.left, target) and self.dfs(root.right, target):
            
            return True
        
        return False