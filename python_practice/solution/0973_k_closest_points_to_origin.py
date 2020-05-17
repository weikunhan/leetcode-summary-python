import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        value_pq = [] 
        res = []
        
        for a, b in points:
            temp_value = a * a + b * b
            
            if len(value_pq) == K:
                heapq.heappushpop(value_pq, (-temp_value, a, b))
            else:
                heapq.heappush(value_pq, (-temp_value, a, b))
                
        for _, a, b in value_pq:
            res.append([a, b])
            
        return res