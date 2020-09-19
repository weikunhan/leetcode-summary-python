class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        value_list = sorted(A)
        temp_value = 0
        res = 0
        
        for value in value_list:
            res += max(temp_value - value, 0)
            temp_value = max(temp_value + 1, value + 1)
            
        return res