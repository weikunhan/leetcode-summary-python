import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        
        value_pq = sticks[:]
        heapq.heapify(value_pq)
        res = 0
        
        while len(value_pq) > 1:
            temp_value = heapq.heappop(value_pq) + heapq.heappop(value_pq)
            heapq.heappush(value_pq, temp_value)
            res += temp_value
            
        return res