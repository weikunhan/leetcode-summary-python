# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.preorder_dfs(preorder, inorder)
        
        return self.res
        
    def preorder_dfs(self, preorder, inorder):
        if not preorder:
            
            return 
        
        root = TreeNode(preorder[0])
        index_value = inorder.index(preorder[0])
        root.left = self.preorder_dfs(preorder[1:index_value + 1], inorder[:index_value])
        root.right = self.preorder_dfs(preorder[index_value + 1:], inorder[index_value + 1:])
        
        return root