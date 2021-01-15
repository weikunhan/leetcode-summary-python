# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        
        self.value_dict = {1: [TreeNode(0)]}
        self.res = 0
        
        self.res = self.dfs(N)

        return self.res
    
    def dfs(self, N):
        temp_list = []
        
        if N in self.value_dict:
            temp_list = self.value_dict[N]
            
            return temp_list
        
        for i in range(1, N, 2):
            for left in self.dfs(i):
                for right in self.dfs(N - 1 - i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    temp_list.append(root)
                    
        self.value_dict[N] = temp_list
        
        return temp_list