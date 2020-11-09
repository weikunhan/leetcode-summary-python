# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        self.res = 0
        
        self.res = self.dfs(root, sum)
        
        return self.res
    
    def dfs(self, root, target):
        temp_value = 0
        
        if not root:    
            
            return temp_value

        temp_value = self.dfs(root.left, target) + self.dfs(root.right, target) + self.postorder(root, target)
        
        return temp_value
        
    def postorder(self, root, target):
        temp_value = 0
        
        if not root:    
            
            return temp_value

        left_value = self.postorder(root.left, target - root.val)
        right_value = self.postorder(root.right, target - root.val)
        temp_value = left_value + right_value
        
        if root.val == target:
            temp_value += 1
        
        return temp_value