# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.res = []
        
        self.preorder(root, 0)
        
        return self.res
    
    def preorder(self, root, count):
        if not root:
            
            return
        
        if count == len(self.res):
            self.res.append(root.val)
            
        self.preorder(root.right, count + 1)
        self.preorder(root.left, count + 1)