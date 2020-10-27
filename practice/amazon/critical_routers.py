""" Critical Routers

You are given an undirected connected graph. 
An articulation point (or cut vertex) is defined as a vertex which, 
when removed along with associated edges, makes the graph disconnected 
(or more precisely, increases the number of connected components in the graph). 
The task is to find all articulation points in the given graph.
Input:
The input to the function/method consists of three arguments:
- numNodes, an integer representing the number of nodes in the graph.
- numEdges, an integer representing the number of edges in the graph.
- edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
Output:
- Return a list of integers representing the critical nodes.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/436073/

Time complexity: O(v(v + e))
Space complexity: O(v)

Example 1:
Input: 
numNodes = 7
numEdges = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
Output: 
[2, 3, 5]
"""

import collections

class Solution(object):
    def critical_routers(self, numNodes, numEdges, edges):
        """
        :type numNodes: int
        :type numEdges: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        self.value_graph = collections.defaultdict(list)
        self.value_list = [-1] * numNodes
        self.res = []

        for i in range(numEdges):
            node, neighbor = edges[i]
            self.value_graph[node].append(neighbor)
            self.value_graph[neighbor].append(node) 

        self.dfs(0, 0, 0)
        self.res = sorted(self.res)

        return self.res

    def dfs(self, node, neighbor, count):
        self.value_list[neighbor] = count + 1
        
        for temp_node in self.value_graph[neighbor]:
            if node == temp_node:
                continue
            elif self.value_list[temp_node] == -1:
                temp_value = self.dfs(neighbor, temp_node, count + 1)
                self.value_list[neighbor] = min(self.value_list[neighbor], temp_value)
            else:
                self.value_list[neighbor] = min(self.value_list[neighbor], self.value_list[temp_node])
                
        if self.value_list[neighbor] == count + 1 and neighbor:
            self.res.append(node)
                
        return self.value_list[neighbor]


def main():
    numNodes = 7
    numEdges = 7
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
    solution = Solution()
    res = solution.critical_routers(numNodes, numEdges, edges)
    print(res)

if __name__ == "__main__": 
    main()