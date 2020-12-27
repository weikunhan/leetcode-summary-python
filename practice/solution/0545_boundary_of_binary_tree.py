# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.temp_root = root
        self.res = []
        
        if not root:
            
            return self.res
        
        self.res.append(root.val)
        self.preorder(root.left)
        self.inorder(root)
        self.postorder(root.right)
        
        return self.res
    
    def preorder(self, root):
        if not root:
            
            return 
        
        if not root.left and not root.right:
            
            return 
        
        self.res.append(root.val)    

        if root.left:
            self.preorder(root.left)
        else:
            self.preorder(root.right)
        
    def inorder(self, root):
        if not root:
            
            return 
        
        self.inorder(root.left)
        
        if root != self.temp_root and not root.left and not root.right:
            self.res.append(root.val)
            
        
        self.inorder(root.right)
        
    def postorder(self, root):
        if not root:
            
            return 
        
        if not root.left and not root.right:
            
            return 
        
        if root.right:
            self.postorder(root.right)
        else:
            self.postorder(root.left)
            
        self.res.append(root.val)