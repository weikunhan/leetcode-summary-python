"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

import collections

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        dummy_head = Node(-1, head)
        value_dict = collections.defaultdict(lambda: Node(-1))
        value_dict[None] = None
        current = head
        
        while current:
            value_dict[current].val = current.val
            value_dict[current].next = value_dict[current.next]
            value_dict[current].random = value_dict[current.random]
            current = current.next
            
        return value_dict[dummy_head.next]