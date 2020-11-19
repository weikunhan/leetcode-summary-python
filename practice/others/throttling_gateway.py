""" Throttling Gateway

Non-Critical requests for a transaction system are routed through a throttling 
gateway to ensure that the network is not choked by non-essential requests.

The gateway has limits as follows:

1. The number of transactions in any given second cannot exceed 3.
2. The number of transactions in any given 10 second period cannot exceed 20. A
   10 seconds period would count all transactions arriving from any time T to
   T + 9 (inclusive of both) for any valid time T.
3. The number of transaction in any given minute cannot exceed 60 (similar to 
   above, 1 minutes is from T to T + 59)

Any request that exceeds any of the above limits will be dropped by the gateway
Given the times at which different requests arrive (sorted in ascending order of 
arrivals), find how many of them will be dropped.

Note: Even if a request is dropped it is till considered for future calculations.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-610975-1-1.html

Time complexity: O(n^2)
Space complexity: O(n)

Input: 
n = 22
requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 11, 11, 11]
Output: 
1
Explanation:
There are total 22 requset. 19 requset within 10 sec which no need to drop.
There are four requests in the first secound. One of them will be dropped as 4 > 3
"""

import collections

class Solution(object):
    def throttling_gateway(self, n, requestTime):
        """
        :type n: int
        :type requestTime: int
        :rtype: int
        """

        pair_value_list = [(1, 3), (10, 20), (60, 60)]
        unique_value_dict = set()
        count_value_dict = collections.Counter(requestTime)
        max_length = max(requestTime)
        presum_value_list = [0] * (max_length + 1)
        res = 0  

        if not requestTime:
            
            return res
        
        for i in range(1, max_length + 1):
            presum_value_list[i] = presum_value_list[i - 1] + count_value_dict[i]

        for state, capacity in pair_value_list:
            window_value = min(state, max_length)
            
            for i in range(max_length - window_value + 1):
                request_value = presum_value_list[i + window_value] - presum_value_list[i]
                temp_value = max(0, request_value - capacity)
                
                for j in range(1, temp_value + 1):
                    unique_value_dict.add(presum_value_list[i + window_value] - j)
        
        res = len(unique_value_dict)
        
        return res

def main(): 
    n = 22
    requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 11, 11, 11]
    solution = Solution()
    res = solution.throttling_gateway(n, requestTime)
    print(res)

if __name__ == "__main__": 
    main()