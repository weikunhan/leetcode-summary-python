# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        left = head
        right = dummy_head
        
        while left and left.next:
            if left.val == left.next.val:
                left = left.next
                right.next = left
            else:
                left = left.next
                right = right.next

        return dummy_head.next