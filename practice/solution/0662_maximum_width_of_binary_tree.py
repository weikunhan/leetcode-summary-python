import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = 0
        value_list = collections.deque([(root, 0)])
        
        if not root:
            
            return res
        
        while value_list:
            temp_value = len(value_list)
            res = max(res, value_list[-1][1] - value_list[0][1] + 1)
            
            for _ in range(temp_value):
                root, cost = value_list.popleft()
         
                if root.left:
                    value_list.append((root.left, cost * 2))

                if root.right:
                    value_list.append((root.right, cost * 2 + 1))

        return res