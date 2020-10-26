import collections
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
          
        value_graph = collections.defaultdict(dict)
        value_pq = []
        heapq.heappush(value_pq, (0, src, K + 1))
        res = -1
        
        for node, neighbor, cost in flights:
            value_graph[node][neighbor] = cost
        
        while value_pq:
            cost, temp_node, K = heapq.heappop(value_pq)
            
            if temp_node == dst: 
                res = cost
                
                return res
            
            if K > 0:
                for neighbor in value_graph[temp_node]:
                    heapq.heappush(value_pq, (cost + value_graph[temp_node][neighbor], neighbor, K - 1))
        
        return res