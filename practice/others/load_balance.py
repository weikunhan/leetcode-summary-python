""" Load Balance

Given a int servers and a int array arrival time and int array work load time. 
Therefore, the finishing time is (arrival time + work load time). 
The servers take task in a robin round manner (plus if the server is still 
working another task, then skip to next server util find the next avaible or 
wait unitil next avaible server). Simulate the servers handling tasks and 
find out which server has a heaviest work load. (Here, the work load is total 
assignied load on this server)

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-627760-1-1.html

Time complexity:  O(nlogn)
Space complexity: O(n)

Example 1:
Input: 
servers = 2
arrivals = [10, 7, 6, 20]
loads = [60, 2, 1, 100]
Output: 
[1]
Explanation:
The first wrok is [6, 1] and finish at 7 using server 0. 
The second wrok is [7, 2] and finish at 9 using server 1. 
server 0 finish and add it into queue again.
The third wrok is [10, 60] and finish at 70 using server 0.
server 1 finish and add it into queue again.
The last work is [20, 100] and finish at 120 using server 1.
Total server 0 = 61, Total sever 1 = 102

Example 2:
Input: 
servers = 1
arrivals = [10, 7, 6, 20]
loads = [60, 2, 1000, 100]
Output: 
[0]
Explanation: 
Only one sever avalible and the left tasks need to wait for excution

Example 3:
Input: 
servers = 0
arrivals = [10, 7, 6, 20]
loads = [60, 2, 1000, 100]
Output: 
[]

Example 4:
Input: 
servers = 3
arrivals = [10, 7, 6, 20]
loads = [1000, 1000, 1000, 1000]
output:
[0, 1, 2]
Explanation: 
Each server has same heaviest work load, return the serve list with ascending order
"""

import heapq
import collections

class Solution(object):
    def load_balance(self, servers, arrivals, loads):
        """
        :type servers: int
        :type arrivals: List[int]
        :type loads: List[int]
        :rtype: List[int]
        """

        server_value_list = collections.deque(range(servers))
        value_dict = collections.Counter()
        task_value_list = sorted(zip(arrivals, loads))
        res = []

        if not servers:

            return res

        value_pq = [(task_value_list[0][0] + task_value_list[0][1], 
                     server_value_list.popleft())]
        value_dict[value_pq[0][1]] = task_value_list[0][1]

        for task in task_value_list[1:]:
            if task[0] < value_pq[0][0]:
                if server_value_list:
                    server_value = server_value_list.popleft()
                    heapq.heappush(value_pq, (task[0] + task[1], server_value))
                    value_dict[server_value] += task[1]
            else:
                server_value_list.append(heapq.heappop(value_pq)[1])
                server_value = server_value_list.popleft()
                heapq.heappush(value_pq, (task[0] + task[1], server_value))
                value_dict[server_value] += task[1]
            
        for key, value in value_dict.items():
            if value == value_dict.most_common()[0][1]:
                res.append(key)

        res = sorted(res)

        return res

def main(): 
    servers = 2
    arrivals = [10, 7, 6, 20]
    loads = [60, 2, 1, 100]
    solution = Solution()
    res = solution.load_balance(servers, arrivals, loads)
    print(res)

if __name__ == "__main__": 
    main()