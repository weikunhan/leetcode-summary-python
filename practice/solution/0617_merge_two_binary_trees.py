# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.dfs(t1, t2)
        
        return self.res
    
    def dfs(self, root_t1, root_t2):        
        if not root_t1 or not root_t2:
            if root_t1 == root_t2:
                
                return None
            else:
                if root_t1:
                    
                    return root_t1
                else:
                    
                    return root_t2
            
        root = TreeNode(root_t1.val + root_t2.val)
        root.left = self.dfs(root_t1.left, root_t2.left)
        root.right = self.dfs(root_t1.right, root_t2.right)
        
        return root