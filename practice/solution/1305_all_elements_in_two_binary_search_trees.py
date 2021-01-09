# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        
        self.res = []
        self.value_pq = []
        
        self.inorder(root1)
        self.inorder(root2)
        
        while self.value_pq:
            self.res.append(heapq.heappop(self.value_pq))
            
        return self.res
    
    def inorder(self, root):
        if not root:
            
            return 
        
        self.inorder(root.left)
        heapq.heappush(self.value_pq, root.val)
        self.inorder(root.right)