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
        temp_res = dummy_head.next
        value_dict = collections.defaultdict(lambda: Node(-1))
        value_dict[None] = None

        while temp_res:
            value_dict[temp_res].val = temp_res.val
            value_dict[temp_res].next = value_dict[temp_res.next]
            value_dict[temp_res].random = value_dict[temp_res.random]
            temp_res = temp_res.next
            
        return value_dict[dummy_head.next]