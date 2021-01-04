# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        right = dummy_head.next
        left = dummy_head
        
        while right and right.next:
            if right.val == right.next.val:
                right = right.next
                left.next = right
            else:
                left = left.next
                right = right.next
                
        return dummy_head.next