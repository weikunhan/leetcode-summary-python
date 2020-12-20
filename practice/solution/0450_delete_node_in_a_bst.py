# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.dfs(root, key)
        
        return self.res
        
    def dfs(self, root, key):
        if not root:
            
            return 
        
        if root.val == key:
            if not root.left:
                
                return root.right
            else:
                temp_root = root.left
                
                while temp_root.right:
                    temp_root = temp_root.right
                    
                root.val = temp_root.val
                root.left = self.dfs(root.left, temp_root.val)
        elif root.val > key:
            root.left = self.dfs(root.left, key)
        else:
            root.right = self.dfs(root.right, key)
            
        return root