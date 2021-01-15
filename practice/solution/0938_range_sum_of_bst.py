# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        self.res = 0
        
        self.inorder(root, low, high)
        
        return self.res
    
    def inorder(self, root, low, high):
        if not root:
            
            return
        
        self.inorder(root.left, low, high)
        
        if low <= root.val <= high:
            self.res += root.val
            
        self.inorder(root.right, low, high)