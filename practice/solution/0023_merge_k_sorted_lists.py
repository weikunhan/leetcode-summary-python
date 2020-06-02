# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        temp_res = dummy_head
        value_pq = [] 
        
        for current in lists:
            if current:
                heapq.heappush(value_pq, (current.val, current))
                
        while value_pq:
            temp_res.next = heapq.heappop(value_pq)[1]
            temp_res = temp_res.next
            
            if temp_res.next:
                heapq.heappush(value_pq, (temp_res.next.val, temp_res.next))
        
        return dummy_head.next   