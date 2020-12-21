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
    
    def preorder(self, root, start, target):
        if not root:
            
            return 
        
        if root.val == target:
            start += 1
        else:
            start = 1
            
        self.res = max(self.res, start)
        self.preorder(root.left, start, root.val + 1)
        self.preorder(root.right, start, root.val + 1)