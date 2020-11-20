# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        a_dummy_head = ListNode(-1)
        b_dummy_head = ListNode(-1)
        left = a_dummy_head
        right = b_dummy_head
        
        while head:
            left.next = head
            right.next = head.next
            left = left.next
            right = right.next
            
            if head.next:
                head = head.next.next
            else:
                head = head.next
        
        left.next = b_dummy_head.next
        
        return a_dummy_head.next