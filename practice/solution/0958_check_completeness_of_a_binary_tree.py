# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        value_list = collections.deque([root])
        sign = 1
        res = False
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                temp_root = value_list.popleft()
                
                if not temp_root:
                    sign = 0
                    continue
               
                if not sign:
                    
                    return res

                value_list.append(temp_root.left)
                value_list.append(temp_root.right)
            
        res = True
        
        return res