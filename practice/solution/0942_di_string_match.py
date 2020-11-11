import collections

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        value_list = collections.deque(range(len(S) + 1))               
        res = []
        
        for char in S:
            if char == 'I': 
                res.append(value_list.popleft())
                
            if char == 'D': 
                res.append(value_list.pop())                
        
        res.append(value_list.pop())
        
        return res