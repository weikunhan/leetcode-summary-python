# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        left = dummy_head.next
        right = dummy_head.next
        res = False
        
        while right and right.next:
            right = right.next.next
            left = left.next        
        
        l1 = left
        l2 = None
        
        while l1:
            temp = l1.next
            l1.next = l2
            l2 = l1
            l1 = temp
            
        left = l2
            
        while left:
            if left.val != head.val:
                
                return res
            
            left = left.next
            head = head.next
            
        res = True
        
        return res