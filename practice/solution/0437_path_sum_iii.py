# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        self.res = 0
        
        self.preorder(root, sum)
        
        return self.res
    
    def preorder(self, root, target):
        if not root:
            
            return 
        
        self.helper(root, target)
        self.preorder(root.left, target)
        self.preorder(root.right, target)
    
    def helper(self, root, target):
        if not root:
            
            return 
        
        if root.val == target:
            self.res += 1
            
        self.helper(root.left, target - root.val)
        self.helper(root.right, target - root.val)