# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.preorder(0, len(nums) - 1, nums)
        
        return self.res
    
    def preorder(self, start, end, value_list):
        if start > end:
            
            return 
        
        index_value = (start + end) // 2
        root = TreeNode(value_list[index_value])
        root.left = self.preorder(start, index_value - 1, value_list)
        root.right = self.preorder(index_value + 1, end, value_list)
        
        return root