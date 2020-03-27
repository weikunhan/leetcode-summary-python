""" Critical Connections

https://leetcode.com/problems/critical-connections-in-a-network/

Given an underected connected graph with n nodes labeled 1..n. 
A bridge (cut edge) is defined as an edge which, when removed, 
makes the graph disconnected (or more precisely, 
increases the number of connected components in the graph). 
Equivalently, an edge is a bridge if and only if it is not contained in any cycle. 
The task is to find all bridges in the given graph. 
Output an empty list if there are no bridges.
Input:
- n, an int representing the total number of nodes.
- edges, a list of pairs of integers representing the nodes connected by an edge.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/372581

Time complexity: O(n)
Space complexity: O(n)

Example 1:
Input: 
n = 5
edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
Output: 
[[1, 2], [4, 5]]
Explanation:
There are 2 bridges:
1. Between node 1 and 2
2. Between node 4 and 5
If we remove these edges, then the graph will be disconnected.
If we remove any of the remaining edges, the graph will remain connected.

Example 2:
Input: 
n = 6
edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
Output: 
[]
Explanation:
We can remove any edge, the graph will remain connected.

Example 3:
Input: 
n = 9
edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
Output: 
[[3, 4], [3, 6], [4, 5]]
"""

import collections

class Solution(object):
    def critical_connections(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        self.value_list = [-1] * n
        self.value_graph = collections.defaultdict(list)
        self.res = []
        
        for a, b in edges:
            self.value_graph[a - 1].append(b - 1)
            self.value_graph[b - 1].append(a - 1)
        
        self.dfs(-1, 0, 0)
        self.res = sorted(self.res)

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
            self.res.append([a + 1, b + 1])
                
        return self.value_list[b]

def main():
    n = 9
    edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
    solution = Solution()
    res = solution.critical_connections(n, edges)
    print(res)

if __name__ == "__main__": 
    main()