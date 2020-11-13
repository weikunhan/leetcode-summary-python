# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        self.res = None
 
        self.res = self.preorder(preorder, inorder)
        
        return self.res
    
    def preorder(self, preorder, inorder):
        if not preorder:
            
            return 
        
        temp_value = preorder[0]
        root = TreeNode(temp_value)
        index_value = inorder.index(temp_value)
        root.left = self.preorder(preorder[1:index_value + 1], inorder[:index_value])
        root.right = self.preorder(preorder[index_value + 1:], inorder[index_value + 1:])
        
        return root