# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.res = []
        
        self.preorder(root)
        
        return self.res
    
    def preorder(self, root):
        if not root:
            
            return 
        
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)