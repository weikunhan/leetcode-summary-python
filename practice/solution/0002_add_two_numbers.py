# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        dummy_head = ListNode(-1)
        temp_res = dummy_head
        
        while l1 or l2 or carry:
            sum_value = carry
            
            if l1:
                sum_value += l1.val
                l1 = l1.next
            
            if l2:
                sum_value += l2.val
                l2 = l2.next
                
            carry, remainder = divmod(sum_value, 10)
            temp_res.next = ListNode(remainder)
            temp_res = temp_res.next
            
        return dummy_head.next