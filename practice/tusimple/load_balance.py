""" Load Balance

Given a in array servers and a nest int array tasks.
Each task include two value int arrival time and int work load time. 
tasks= [[arrival_time, work_load_time], ..., [arrival_time, work_load_time]]
Therefore, the finishing time is (arrival time + work load time). 
The servers take task in a robin round manner (plus if the server is still 
working another task, then skip to next server util find the next avaible or 
wait unitil next avaible server). Simulate the servers handling tasks and 
find out which server has a heaviest work load.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-601384-1-1.html

Time complexity:  O(nlogn)
Space complexity: O(n)

Example 1:
Input: 
servers = [1, 2, 3, 4, 5, 6]
tasks = [[10, 60], [7, 2], [6, 1], [20, 100]]
Output: 
[2, 100]
Explanation:
The heaviest work load is [20, 100] and it locate in server 2. Therefore, 
return pair [severid, work load]
The first wrok is [6, 1] and finish at 7 using server 1. 
The second wrok is [7, 2] and finish at 9 still using server 1.
The third wrok is [10, 60] and finish at 70 still using server 1.
The last work is [20, 100] and finish at 120. Since server 1 is not empty, it
using sever 2.

Example 2:
Input: 
servers = [1]
tasks = [[10, 60], [7, 2], [6, 1000], [20, 100]]
Output: 
[1, 1000]
Explanation: 
Only one sever avalible and the left tasks need to wait for excution

Example 3:
Input: 
servers = []
tasks = [[10, 60], [7, 2], [6, 1000], [20, 100]]
Output: 
[]

Example 4:
Input: 
servers = [1, 2, 3, 4, 5, 6]
tasks = [[10, 1000], [7, 1000], [6, 1000], [20, 1000]]
output:
[1, 1000]
Explanation: 
Each server has same heaviest work load, return the serve with smallest number 
"""

import heapq

class Solution(object):
    def load_balance(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[List[int]]
        :rtype: List[int]
        """

        serve_value_pq = servers
        res = []

        if not serve_value_pq:

            return res

        heapq.heapify(serve_value_pq)
        value_list = sorted(tasks)
        value_pq = [(value_list[0][0] + value_list[0][1], 
                     heapq.heappop(serve_value_pq))]
        res = [value_pq[0][1], value_list[0][1]]

        for task in value_list[1:]:
            if task[0] < value_pq[0][0]:
                if serve_value_pq:
                    serve_value = heapq.heappop(serve_value_pq)
                    heapq.heappush(value_pq, (task[0] + task[1], serve_value))
                    
                    if res[1] < task[1]:
                        res = [serve_value, task[1]]
                else:

                    return res
            else:
                _, serve_value = heapq.heappop(value_pq)
                heapq.heappush(value_pq, (task[0] + task[1], serve_value))
                
                if res[1] < task[1]:
                    res = [serve_value, task[1]]

        return res

def main(): 
    servers = [1, 2, 3, 4, 5, 6]
    tasks = [[10, 1000], [7, 1000], [6, 1000], [20, 1000]]
    solution = Solution()
    res = solution.load_balance(servers, tasks)
    print(res)

if __name__ == "__main__": 
    main()