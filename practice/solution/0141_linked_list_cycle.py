# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        left = dummy_head
        right = dummy_head
        res = False
        
        while right and right.next:
            left = left.next
            right = right.next.next
            
            if left == right:
                res = True
                
                return res
        
        return res