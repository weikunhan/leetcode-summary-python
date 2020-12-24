# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        self.res = None
        
        self.res = self.preorder(head)
        
        return self.res
    
    def preorder(self, head):
        if not head:
            
            return 
        
        if not head.next:
            
            return TreeNode(head.val)
        
        left = head
        right = head.next.next
        
        while right and right.next:
            left = left.next
            right = right.next.next
            
        temp = left.next
        left.next = None
        root = TreeNode(temp.val)
        root.left = self.preorder(head)
        root.right = self.preorder(temp.next)
        
        return root