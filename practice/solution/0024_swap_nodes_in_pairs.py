# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        left = dummy_head
        right = dummy_head.next

        while left.next and right.next:
            l1 = left.next
            l2 = right.next
            l1.next = l2.next
            l2.next = l1
            left.next = l2
            left = l1
            right = l1.next
        
        return dummy_head.next