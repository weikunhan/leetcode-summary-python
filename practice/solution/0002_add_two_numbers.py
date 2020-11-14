# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        temp_res = dummy_head
        carry = 0 
        
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
                
            if l2:
                carry += l2.val
                l2 = l2.next
                
            carry, remainder = divmod(carry, 10)
            temp_res.next = ListNode(remainder)
            temp_res = temp_res.next
            
        return dummy_head.next