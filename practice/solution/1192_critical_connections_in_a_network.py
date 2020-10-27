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
        
        for node, neighbor in connections:
            self.value_graph[node].append(neighbor)
            self.value_graph[neighbor].append(node)
        
        self.dfs(0, 0, 0)
        
        return self.res
    
    def dfs(self, node, neighbor, count):
        self.value_list[neighbor] = count + 1
        
        for temp_node in self.value_graph[neighbor]:
            if node == temp_node:
                continue
            elif self.value_list[temp_node] == -1:
                temp_value = self.dfs(neighbor, temp_node, count + 1)
                self.value_list[neighbor] = min(temp_value, self.value_list[neighbor])
            else:
                self.value_list[neighbor] = min(self.value_list[neighbor], self.value_list[temp_node])
                
        if self.value_list[neighbor] == count + 1 and neighbor:
            self.res.append([node, neighbor])
            
        return self.value_list[neighbor]
        