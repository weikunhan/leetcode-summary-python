# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        self.temp_value = None
        
        self.postorder(root)
        
    def postorder(self, root):
        if not root:
            
            return
        
        self.postorder(root.right)
        self.postorder(root.left)
        root.right = self.temp_value
        root.left = None
        self.temp_value = root