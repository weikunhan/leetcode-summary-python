# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        
        self.postorder(root)
        
        return self.res
    
    def postorder(self, root):
        temp_value = 0
        
        if not root:
            
            return temp_value
        
        left_value = self.postorder(root.left)
        right_value = self.postorder(root.right)
        temp_value = 1 + max(left_value, right_value)
        self.res = max(self.res, left_value + right_value)
        
        return temp_value