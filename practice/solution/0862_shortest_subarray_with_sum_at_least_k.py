import collections

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        value_list = collections.deque([(0, 0)])
        sum_value = 0
        res = sys.maxsize

        for i in range(len(A)):
            sum_value += A[i]
            
            while value_list and sum_value - value_list[0][1] >= K:
                res = min(res, i - value_list.popleft()[0] + 1)
            
            while value_list and sum_value <= value_list[-1][1]:
                value_list.pop()
            
            value_list.append([i + 1, sum_value])
       
        if res == sys.maxsize:
            res = -1

        return res 