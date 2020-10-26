"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

import collections

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        value_list = collections.deque([node])
        value_dict = {}
        res = None
        
        if not node:
            
            return res
        
        value_dict[node] = Node(node.val)
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                temp_node = value_list.popleft()

                for neighbor in temp_node.neighbors:
                    if neighbor not in value_dict:
                        value_dict[neighbor] = Node(neighbor.val)
                        value_dict[temp_node].neighbors.append(value_dict[neighbor])
                        value_list.append(neighbor)
                    else:
                        value_dict[temp_node].neighbors.append(value_dict[neighbor])

        res = value_dict[node]
        
        return res