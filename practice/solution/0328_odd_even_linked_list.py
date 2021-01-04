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
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        left = dummy_head.next
        right = None
        temp_res = None
        
        if not head:
            
            return dummy_head.next
        
        right = left.next
        temp_res = right
        
        while right and right.next:
            left.next = left.next.next
            right.next = right.next.next
            left = left.next
            right = right.next
        
        left.next = temp_res
        
        return dummy_head.next