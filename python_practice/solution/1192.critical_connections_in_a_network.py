import collections

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.value_list = [-1] * n
        self.value_graph = collections.defaultdict(list)
        self.res = []
        
        for a, b in connections:
            self.value_graph[a].append(b)
            self.value_graph[b].append(a)
        
        self.dfs(-1, 0, 0)
        
        return self.res
    
    def dfs(self, a, b, count):
        self.value_list[b] = count + 1
        
        for node in self.value_graph[b]:
            if node == a:
                continue
            elif self.value_list[node] == -1:
                temp_value = self.dfs(b, node, count + 1)
                self.value_list[b] = min(self.value_list[b], temp_value)
            else:
                self.value_list[b] = min(self.value_list[b], self.value_list[node])
                
        if self.value_list[b] == count + 1 and b != 0:
            self.res.append([a, b])
                
        return self.value_list[b]
        