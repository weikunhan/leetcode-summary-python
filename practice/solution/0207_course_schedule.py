import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        value_graph = collections.defaultdict(list)
        value_list = collections.deque()
        degree_value_list = [0] * numCourses
        count = 0
        res = False
        
        for a, b in prerequisites:
            value_graph[b].append(a)
            degree_value_list[a] += 1
            
        for i in range(numCourses):
            if not degree_value_list[i]:
                value_list.append(i)
            
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                temp_root = value_list.popleft()
                count += 1
                
                for neighbor in value_graph[temp_root]:
                    degree_value_list[neighbor] -= 1
                    
                    if not degree_value_list[neighbor]:
                        value_list.append(neighbor)
                        
        if count == numCourses:
            res = True
            
        return res