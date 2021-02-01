# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        temp_res = dummy_head
        left = dummy_head.next
        right = dummy_head.next

        while True:
            count = 0
            
            for _ in range(k): 
                if right:
                    right = right.next
                    count += 1
                
            if count == k:
                l1 = left
                l2 = right
                
                for _ in range(count):
                    temp = l1.next
                    l1.next = l2
                    l2 = l1
                    l1 = temp
                
                temp_res.next = l2
                temp_res = left 
                left = right
            else:
                return dummy_head.next