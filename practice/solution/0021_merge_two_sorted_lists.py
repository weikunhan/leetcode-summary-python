# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        temp_res = dummy_head
        
        while l1 and l2:
            if l1.val > l2.val:
                temp_res.next = l2
                l2 = l2.next
            else:
                temp_res.next = l1
                l1 = l1.next
            
            temp_res = temp_res.next
            
        if l1:
            temp_res.next = l1
        elif l2:
            temp_res.next = l2
        else:
            temp_res.next = None
            
        return dummy_head.next
                