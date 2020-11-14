# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.res = []
        
        self.preorder(root, sum, [])
        
        return self.res
    
    def preorder(self, root, target, value_list):
        if not root:
            
            return
        
        if not root.left and not root.right and target == root.val:
            self.res.append(value_list + [root.val])
            
        self.preorder(root.left, target - root.val, value_list + [root.val])
        self.preorder(root.right, target - root.val, value_list + [root.val])