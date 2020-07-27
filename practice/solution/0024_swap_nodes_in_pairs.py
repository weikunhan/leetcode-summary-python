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
        
        dummy_head = ListNode(None)
        temp_res = dummy_head
        temp_res.next = head
        
        while temp_res.next and temp_res.next.next:
            l1 = temp_res.next
            l2 = l1.next
            temp = l2.next
            l1.next = temp
            l2.next = l1
            temp_res.next = l2
            temp_res = l1
        
        return dummy_head.next