# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        value_dict = collections.defaultdict(list)
        value_list = collections.deque([(root, 0)])
        res = []

        if not root:
            
            return res
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                temp_root, cost = value_list.popleft()
                value_dict[cost].append(temp_root.val)

                if temp_root.left:
                    value_list.append((temp_root.left, cost - 1))

                if temp_root.right:
                    value_list.append((temp_root.right, cost + 1))

        for key, value in sorted(value_dict.items()):
            res.append(value)
            
        return res