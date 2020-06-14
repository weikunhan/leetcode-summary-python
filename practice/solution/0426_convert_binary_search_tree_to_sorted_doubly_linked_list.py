"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        self.res = None
        
        self.res = self.postorder(root)
        
        return self.res
    
    def postorder(self, root):
        if not root:
            
            return None
        
        left_value = self.postorder(root.left)
        right_value = self.postorder(root.right)
        root.left = root
        root.right = root
        node = self.helper(self.helper(left_value, root), right_value)
        
        return node
    
    def helper(self, node_a, node_b):
        if not node_a:
            
            return node_b
        
        if not node_b:
            
            return node_a

        l1 = node_a.left
        l2 = node_b.left
        l1.right = node_b
        node_b.left = l1
        l2.right = node_a
        node_a.left = l2

        return node_a