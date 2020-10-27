# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.res = -sys.maxsize - 1
        
        self.postorder(root)
        
        return self.res
    
    def postorder(self, root):
        temp_list = [0, 0.0]
        
        if not root:
            
            return temp_list
        
        left_value = self.postorder(root.left)
        right_value = self.postorder(root.right)
        temp_value = left_value[0] + right_value[0] + 1
        sum_value = left_value[1] + right_value[1] + root.val
        self.res = max(self.res, sum_value / temp_value)
        temp_list = [temp_value, sum_value]
        
        return temp_list
        