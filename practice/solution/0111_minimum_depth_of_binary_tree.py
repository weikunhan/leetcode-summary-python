# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        value_list = collections.deque([(root, 1)])
        res = 0
        
        if not root:
            
            return res
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                temp_root, cost = value_list.popleft()
                
                if not temp_root.left and not temp_root.right:
                    res = cost
                    
                    return res
                
                if temp_root.left:
                    value_list.append((temp_root.left, cost + 1))
                    
                if temp_root.right:
                    value_list.append((temp_root.right, cost + 1))
                    
        return res