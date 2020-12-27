# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.preorder(s)
        
        return self.res
    
    def preorder(self, s):
        if not s:
            
            return 
        
        if not '(' in s:
            
            return TreeNode(int(s))
        
        index_value = s.index('(')
        temp_value = 0
        count = 0
        
        while count < len(s):
            if s[count] == '(':
                temp_value += 1
            
            if s[count] == ')':
                temp_value -= 1
                
            if count > index_value and not temp_value:
                break
                
            count += 1
                
        root = TreeNode(s[:index_value])
        root.left = self.preorder(s[index_value + 1: count])
        root.right = self.preorder(s[count + 2: -1])
        
        return root