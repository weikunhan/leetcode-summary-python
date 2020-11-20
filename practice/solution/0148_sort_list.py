# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        self.res = None
        
        self.res = self.dfs(head)
        
        return self.res
    
    def dfs(self, head):
        if not head or not head.next:
            
            return head        

        left = head
        right = head.next
        
        while right and right.next:
            right = right.next.next
            left = left.next
            
        temp = left.next
        left.next = None
        l1 = self.dfs(head)
        l2 = self.dfs(temp)
        
        return self.helper(l1, l2)        
    
    def helper(self, l1, l2):
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
        
        if l2:
            temp_res.next = l2
            
        return dummy_head.next