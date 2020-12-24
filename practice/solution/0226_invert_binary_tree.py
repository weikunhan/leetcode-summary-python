# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.postorder(root)
        
        return self.res
    
    def postorder(self, root):
        if not root:
            
            return 
        
        temp_root = root.left
        root.left = self.postorder(root.right)
        root.right = self.postorder(temp_root)
        
        return root        