class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        
        value_list = A
        right_sum_value = 0
        left_sum_value = 0
        res = 0
        
        for i in range(1, len(A)):
            value_list[i] += value_list[i - 1]
        
        left_sum_value = value_list[L - 1]
        right_sum_value = value_list[M - 1]
        res = value_list[L + M - 1]
        
        for i in range(L + M, len(value_list)):
            left_sum_value = max(left_sum_value, value_list[i - M] - value_list[i - L - M])
            right_sum_value = max(right_sum_value, value_list[i - L] - value_list[i - L - M])
            res = max(res, left_sum_value + value_list[i] - value_list[i - M], right_sum_value + value_list[i] - value_list[i - L])
            
        return res