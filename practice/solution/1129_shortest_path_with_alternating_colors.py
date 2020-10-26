import collections

class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """

        value_graph = collections.defaultdict(lambda: collections.defaultdict(set))
        value_list = collections.deque([(0, 1, 0), (0, -1, 0)])
        res = [sys.maxsize] * n
        
        for node, neighbor in red_edges:
            value_graph[node][1].add(neighbor)
            
        for node, neighbor in blue_edges:
            value_graph[node][-1].add(neighbor)
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                temp_node, color, cost = value_list.popleft()
                res[temp_node] = min(cost, res[temp_node])
                color *= -1
                
                for neighbor in list(value_graph[temp_node][color]):
                    value_graph[temp_node][color].remove(neighbor)
                    value_list.append((neighbor, color, cost + 1))
                    
        for i in range(len(res)):
            if res[i] == sys.maxsize:
                res[i] = -1
                
        return res