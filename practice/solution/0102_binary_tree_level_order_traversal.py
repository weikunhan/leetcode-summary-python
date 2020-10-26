# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        value_list = collections.deque([root])
        res = []
        
        if not root:
            
            return res
        
        while value_list:
            temp_value = len(value_list)
            temp_list = []
            
            for _ in range(temp_value):
                root = value_list.popleft()
                temp_list.append(root.val)
                
                if root.left:
                    value_list.append(root.left)
                    
                if root.right:
                    value_list.append(root.right)
                
            res.append(temp_list)  
                    
        return res