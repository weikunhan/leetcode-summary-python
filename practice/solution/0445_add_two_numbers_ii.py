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
        first_value = ''
        second_value = ''
        temp_value = ''
        carry = 0
        left = -1
        right = -1
        
        while l1:
            first_value += str(l1.val)
            l1 = l1.next
            left += 1
            
        while l2:
            second_value += str(l2.val)
            l2 = l2.next
            right += 1
            
        while left >= 0 or right >= 0 or carry: 
            if left >= 0:
                carry += ord(first_value[left]) - ord('0')
                left -= 1
                
            if right >= 0:
                carry += ord(second_value[right]) - ord('0')
                right -= 1
                
            carry, remainder = divmod(carry, 10)
            temp_value = str(remainder) + temp_value
            
        for char in temp_value:
            temp_res.next = ListNode(char)
            temp_res = temp_res.next
            
        return dummy_head.next   