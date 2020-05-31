""" Min Cost to Connect All Nodes

Given an undirected graph with n nodes labeled 1..n. Some of the nodes are 
already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] 
together. Your task is to augment this set of edges with additional edges to 
connect all the nodes. Find the minimum cost to add new edges between the nodes 
such that all the nodes are accessible from each other.
Input:
- n, an int representing the total number of nodes.
- edges, a list of integer pair representing the nodes already connected by an edge.
- newEdges, a list where each element is a triplet representing the pair of 
nodes between which an edge can be added and the cost of addition, respectively 
(e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/356981

Time complexity: O(log*(n))
Space complexity: O(n)

Example 1:
Input: 
n = 6
edges = [[1, 4], [4, 5], [2, 3]]
newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 
7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to 
node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.
"""

class Solution(object):
    def min_cost_to_connect_all_nodes(self, n, edges, newEdges):
        """
        :type n: int
        :type edges: List[List[int]]
        :type newEdges: List[List[int]]
        :rtype: int
        """
        
        self.parent_list = range(n)         
        self.res = 0

        for a, b in edges:
            self.union(a - 1, b - 1, 0)

        self.parent_list = map(self.find, self.parent_list)

        for a, b, cost in sorted(newEdges, key=lambda x: x[2]):
            self.union(a - 1, b - 1, cost) 

        return self.res
    
    def find(self, x):
        if self.parent_list[x] != x:
            self.parent_list[x] = self.find(self.parent_list[x])
            
        return self.parent_list[x]
        
    def union(self, x, y, cost):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            self.res += cost
            self.parent_list[root_x] = root_y

def main(): 
    n = 6
    edges = [[1, 4], [4, 5], [2, 3]]
    newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
    solution = Solution()
    res = solution.min_cost_to_connect_all_nodes(n, edges, newEdges)
    print(res)

if __name__ == "__main__": 
    main()