# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.postorder(root, p, q)
        
        return self.res
    
    def postorder(self, root, root_p, root_q):
        if not root:
            
            return 
        
        left_value = self.postorder(root.left, root_p, root_q)
        right_value = self.postorder(root.right, root_p, root_q)
    
        if root_p == root or root_q == root:
            
            return root
    
        if left_value and right_value:
            
            return root
        
        if left_value:
            
            return left_value
        else:
        
            return right_value