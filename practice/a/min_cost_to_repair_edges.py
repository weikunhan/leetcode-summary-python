""" Min Cost to Repair Edges

There's an undirected connected graph with n nodes labeled 1..n. But some of 
the edges has been broken disconnecting the graph. Find the minimum cost to 
repair the edges so that all the nodes are once again accessible from each other.
Input:
- n, an int representing the total number of nodes.
- edges, a list of integer pair representing the nodes connected by an edge.
- edgesToRepair, a list where each element is a triplet representing the pair of 
nodes between which an edge is currently broken and the cost of repearing that 
edge, respectively (e.g. [1, 2, 12] means to repear an edge between nodes 1 and 
2, the cost would be 12).

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/357310

Time complexity: O(log*n)
Space complexity: O(n)

Example 1:
Input: 
n = 5
edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
Output: 
20
Explanation:
There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
We can connect these components into a single component by repearing the edges 
between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.

Example 2:
Input: 
n = 6
edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
edgesToRepair = [[1, 6, 410], [2, 4, 800]]
Output: 
410

Example 3:
Input: 
n = 6
edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
Output: 
79
"""

class Solution(object):
    def min_cost_to_repair_edges(self, n, edges, edgesToRepair ):
        """
        :type n: int
        :type edges: List[List[int]]
        :type edgesToRepair: List[List[int]]
        :rtype: int
        """

        self.parent_list = range(n)
        value_dict = set()
        self.res = 0

        for a, b, _ in edgesToRepair:
            value_dict.add((a - 1, b - 1))

        for a, b in edges:
            if not (a - 1, b - 1) in value_dict:
                self.union(a - 1, b - 1, 0)

        self.parent_list = map(self.find, self.parent_list)

        for a, b, cost in sorted(edgesToRepair, key=lambda x: x[2]):
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
    n = 5
    edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
    solution = Solution()
    res = solution.min_cost_to_repair_edges(n, edges, edgesToRepair)
    print(res)

if __name__ == "__main__": 
    main()