# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        self.temp_root = TreeNode(-sys.maxsize - 1)
        self.root_first = None
        self.root_second = None
        
        self.inorder(root)
        # temp = self.root_first.val
        # self.root_first.val = self.root_second.val
        # self.root_second.val = temp
        self.root_first.val, self.root_second.val = self.root_second.val, self.root_first.val
        
    def inorder(self, root):
        if not root:
            
            return 
        
        self.inorder(root.left)
        
        if not self.root_first and self.temp_root.val > root.val:
            self.root_first = self.temp_root
            self.root_seond = root
            
        if self.root_first and self.temp_root.val > root.val:
            self.root_second = root
            
        self.temp_root = root
        self.inorder(root.right)