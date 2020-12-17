"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        self.res = None
        
        self.res = self.preorder(root)
        
        return self.res
    
    def preorder(self, root):
        if not root:
            
            return
        
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.helper(root.next)
                
        if root.right:
            root.right.next = self.helper(root.next)
            
        self.preorder(root.right)
        self.preorder(root.left)
        
        return root
            
    def helper(self, root):
        if not root:
            
            return
        
        if root.left:
            
            return root.left
        
        if root.right:
            
            return root.right
        
        return self.helper(root.next)