# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = -sys.maxsize - 1
        
        self.postorder(root)
        
        return self.res

    def postorder(self, root):
        temp_value = 0
        
        if not root:
            
            return temp_value
        
        left_value = self.postorder(root.left)
        right_value = self.postorder(root.right)
        self.res = max(self.res, left_value + root.val + right_value)
        temp_value = max(0, max(left_value + root.val, right_value + root.val))
        
        return temp_value