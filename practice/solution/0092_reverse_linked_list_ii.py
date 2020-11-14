# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        temp_res = dummy_head
        
        if m == n:
            
            return dummy_head.next
        
        for _ in range(m - 1):
            temp_res = temp_res.next
            
        l1 = temp_res.next
        l2 = None
        
        for _ in range(n - m + 1):
            temp = l1.next
            l1.next = l2
            l2 = l1
            l1 = temp
        
        temp_res.next.next = l1    
        temp_res.next = l2    
        
        return dummy_head.next