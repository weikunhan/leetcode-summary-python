class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        res = arr[:]
        
        while True:
            temp_value = res[:1] + [b + (a > b < c) - (a < b > c) for a, b, c in zip(res, res[1:], res[2:])] + res[-1:]
            
            if temp_value == res:
                
                return res
            
            res = temp_value
