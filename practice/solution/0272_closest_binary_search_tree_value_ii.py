# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        
        self.value_pq = []
        self.inorder(root, target)
        self.res = []

        while k:
            self.res.append(heapq.heappop(self.value_pq)[1])
            k -= 1
            
        return self.res

    def inorder(self, root, target):
        if not root:
            
            return 
        
        self.inorder(root.left, target)
        heapq.heappush(self.value_pq, (abs(target - root.val), root.val))
        self.inorder(root.right, target)