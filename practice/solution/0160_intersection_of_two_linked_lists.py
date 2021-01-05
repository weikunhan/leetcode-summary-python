# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        temp_res = dummy_head
        left = headA 
        right = headB

        while left != right:
            if left:
                left = left.next
            else:
                left = headB
                
            if right:
                right = right.next
            else:
                right = headA
                
        temp_res.next = left
        
        return dummy_head.next        