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
        
        dummy_head_1 = ListNode(-1)
        dummy_head_2 = ListNode(-1)
        left = dummy_head_1
        right = dummy_head_2
        
        while head:
            left.next = head
            right.next = head.next
            left = left.next
            right = right.next
            
            if head.next:
                head = head.next.next
            else:
                head = head.next
        
        left.next = dummy_head_2.next
        
        return dummy_head_1.next