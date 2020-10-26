# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        value_list = collections.deque([root])
        res = []
        
        if not root:
            
            return res
        
        while value_list:
            temp_value = len(value_list)
            sum_value = 0.0
            
            for _ in range(temp_value):
                temp_root = value_list.popleft()
                sum_value += temp_root.val
                
                if temp_root.left:
                    value_list.append(temp_root.left)
                    
                if temp_root.right:
                    value_list.append(temp_root.right)
                
            res.append(sum_value / temp_value)
                    
        return res