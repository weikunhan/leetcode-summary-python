""" Subtree with Maximum Average

Given an N-ary tree, find the subtree with the maximum average. 
Return the root of the subtree.

A subtree of a tree is the node which have at least 1 child plus all its 
descendants. The average value of a subtree is the sum of its values, 
divided by the number of nodes.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/349617

Time complexity: O(n)
Space complexity: O(1)

Example 1:
Input:
		 20
	   /   \
	 12     18
  /  |  \   / \
11   2   3 15  8

Output: 
18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125
18 has the maximum average so output 18.
"""

import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def subtree_with_maximum_average(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.res = 0
        self.temp_value = -sys.maxsize - 1

        self.postorder(root)
        
        return self.res
    
    def postorder(self, root):
        if not root:
            temp_list = [0, 0.0]

            return temp_list

        count_value = 0
        sum_value = 0
        
        for child in root.children:
            value_list = self.postorder(child)
            count_value += value_list[0]
            sum_value += value_list[1]
        
        sum_value += root.val
        count_value += 1

        if count_value != 1 and (sum_value / count_value) > self.temp_value:
            self.res = root.val
            self.temp_value = sum_value / count_value

        temp_list = [count_value, sum_value]
        
        return temp_list

def main():
    root8 = TreeNode(8, [])
    root7 = TreeNode(15, [])
    root6 = TreeNode(3, [])
    root5 = TreeNode(2, [])
    root4 = TreeNode(11, [])
    root3 = TreeNode(18, [root7, root8])
    root2 = TreeNode(12, [root4, root5, root6])
    root1 = TreeNode(20, [root2, root3])
    solution = Solution()
    res = solution.subtree_with_maximum_average(root1)
    print(res)

if __name__ == "__main__": 
    main()     
        