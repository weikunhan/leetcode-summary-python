import collections

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        presum_value = 0
        value_dict = collections.Counter()
        value_dict[0] = 1 
        res = 0
        
        for num in A:
            presum_value += num
            res += value_dict[presum_value % K]
            value_dict[presum_value % K] += 1
        
        return res