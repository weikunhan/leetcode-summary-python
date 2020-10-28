""" Min Cost to Racing Track end


There are three racing tracks. The car departs from middle of the racing track. 
There are obstacles on the racing track. Given a int array to indicate which 
racing track have obstacles. Ask at least a few turn cost to end of racing track.


Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-642190-1-1.html

Time complexity:  O(n)
Space complexity: O(1)

Example 1:
Input: 
obstacles = [0, 1]
Output: 
1 
Explanation: 
Start from line 1. The first obstacle in line 0 and not change line 
The second obstacle in line 1 and need to change 1 (cost add 1). Total cost is 1

Example 2:
Input: 
obstacles = [1, 2, 0, 1]
Output: 
3
Explanation:
Start from line 1. The first obstacle in line 1 and need to change line (cost add 1)
The second obstacle in line 2, if you last change to line 2 which need change line 
(cost add 1) and if you last change to line 0 which no need change line.
The Third obstacle in line 0, if you last change to line 0 which need change line 
(cost add 1) and if you last change to line 2.
The fourth obstacle in line 1, if you stay in last line 0 or line 2, you don't
need to change line. Total cost is 3

Example 3:
Input:
obstacles = [0, 1, 1, 2, 1, 2, 1, 1, 0]
Output: 
2
Explanation:
Change line 1 to line 0 and change back to line 1. Total cost is 2.
"""

class Solution(object):
    def min_cost_to_racing_track_end(self, obstacles):
        """
        :type nums: List[int]
        :rtype: int
        """

        value_list = [1, 0, 1]
        count = 0
        res = 0

        while count < len(obstacles):
            if obstacles[count] == 1:
                break
            
            count += 1

        while count < len(obstacles):
            if count > 0 and obstacles[count] == obstacles[count - 1]:
                count += 1
                continue
            
            if count == len(obstacles) - 1:
                value_list[obstacles[count]] += 1
            else: 
                value_list[obstacles[count]] += 2
            
            count += 1
        
        res = min(value_list)

        return res

def main(): 
    obstacles = [0, 1, 1, 2, 1, 2, 1, 1, 0]
    solution = Solution()
    res = solution.min_cost_to_racing_track_end(obstacles)
    print(res)

if __name__ == "__main__": 
    main()