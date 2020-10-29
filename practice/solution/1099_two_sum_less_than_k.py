class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        value_list = sorted(A)
        left = 0
        right = len(value_list) - 1
        res = -1 
        
        while left < right:
            if value_list[left] + value_list[right] < K:
                res = max(res, value_list[left] + value_list[right])
                left += 1
            else:
                right -= 1
        
        return res