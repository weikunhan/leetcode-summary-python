# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.res = []
        
        self.preorder(root, 0)
        
        return self.res
    
    def preorder(self, root, start):
        if not root:
            
            return
        
        if start == len(self.res):
            self.res.append(root.val)
        
        self.preorder(root.right, start + 1)
        self.preorder(root.left, start + 1)