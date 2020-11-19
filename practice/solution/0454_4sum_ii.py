import collections

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        value_dict = collections.Counter()
        res = 0 
        
        for i in range(len(A)):
            for j in range(len(B)):
                temp_value = A[i] + B[j]
                value_dict[temp_value] += 1
                
        for i in range(len(C)):
            for j in range(len(D)):
                temp_value = 0 - (C[i] + D[j])
                res += value_dict[temp_value]
        
        return res