# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        
        self.preorder(root, 0, 0)
        
        return self.res
    
    def preorder(self, root, count, target):
        if not root:
            
            return 
        
        if root.val == target:
            count += 1
        else:
            count = 1
            
        self.res = max(self.res, count)
        self.preorder(root.left, count, root.val + 1)
        self.preorder(root.right, count, root.val + 1)