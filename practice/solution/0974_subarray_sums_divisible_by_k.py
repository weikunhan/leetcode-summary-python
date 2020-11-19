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
        
        for value in A:
            presum_value = (presum_value + value) % K
            res += value_dict[presum_value]
            value_dict[presum_value] += 1
        
        return res