"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        self.res = None
        
        self.res = self.dfs(node.right)
        
        if self.res:
            
            return self.res
        
        while node.parent and node.parent.val < node.val:
            node = node.parent
            
        self.res = node.parent
        
        return self.res
    
    def dfs(self, root):
        if not root:
            
            return 
        
        if root.left:
            
            return self.dfs(root.left)
        
        return root