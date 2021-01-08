import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        self.value_dict = collections.defaultdict(list)
        self.res = []
        
        self.postorder(root)
        
        for key, value in self.value_dict.items():
            if len(value) >= 2:
                self.res.append(value[0])
            
        return self.res
                
    def postorder(self, root):
        temp_value = '#'
        
        if not root:
            
            return temp_value
        
        left_value = self.postorder(root.left)
        right_value = self.postorder(root.right)
        temp_value = left_value + ' ' + right_value + ' ' + str(root.val)
        self.value_dict[temp_value].append(root)
        
        return temp_value