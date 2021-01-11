# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        self.res = None
        self.count = 0
        
        self.res = self.preorder_dfs(preorder, sys.maxsize)
        
        return self.res

    def preorder_dfs(self, preorder, target):
        if self.count == len(preorder):
            
            return 
        
        if preorder[self.count] > target:
            
            return
        
        root = TreeNode(preorder[self.count])
        self.count += 1
        root.left = self.preorder_dfs(preorder, root.val)
        root.right = self.preorder_dfs(preorder, target)
        
        return root