# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.value_list = []
        self.res = False
        
        self.inorder(root)
        
        for i in range(1, len(self.value_list)):
            if self.value_list[i] <= self.value_list[i - 1]:
                
                return self.res
            
        self.res = True
        
        return self.res
        
    def inorder(self, root):
        if not root:
            
            return 
        
        self.inorder(root.left)
        self.value_list.append(root.val)
        self.inorder(root.right)