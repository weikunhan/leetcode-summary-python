# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        self.count = k 
        self.res = None
        
        self.inorder(root)
        
        return self.res

    def inorder(self, root):
        if not root:
            
            return
        
        self.inorder(root.left)
        self.count -= 1
        
        if not self.count:
            self.res = root.val
        
        self.inorder(root.right)