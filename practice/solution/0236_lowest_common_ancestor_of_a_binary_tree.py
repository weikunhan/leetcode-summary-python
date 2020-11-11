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
    
    def postorder(self, root, p_root, q_root):
        if not root:
            
            return 
        
        if p_root == root or q_root == root:
            
            return root
        
        left_value = self.postorder(root.left, p_root, q_root)
        right_value = self.postorder(root.right, p_root, q_root)
        
        if left_value and right_value:
            
            return root
        
        if not left_value:
            
            return right_value
        
        if not right_value:
            
            return left_value