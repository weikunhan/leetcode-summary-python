# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        temp_res = dummy_head
        left = dummy_head.next
        right = dummy_head.next
        
        while right and right.next:
            right = right.next.next
            left = left.next
            
        temp_res.next = left
            
        return dummy_head.next