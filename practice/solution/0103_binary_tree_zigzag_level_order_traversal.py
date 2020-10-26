# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        value_list = collections.deque([root])
        sign = 1
        res = []
        
        if not root:
            
            return res
        
        while value_list:
            temp_value = len(value_list)
            temp_list = []
            
            for _ in range(temp_value):
                temp_root = value_list.popleft()
                temp_list.append(temp_root.val)
                
                if temp_root.left:
                    value_list.append(temp_root.left)
                    
                if temp_root.right:
                    value_list.append(temp_root.right)
                    
            res.append(temp_list[::sign])
            sign *= -1
            
        return res