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
            root.left.next = root.right
           
        if root.right and root.next:
            root.right.next = root.next.left
        
        self.preorder(root.left)
        self.preorder(root.right)
        
        return root