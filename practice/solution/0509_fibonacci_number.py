class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        end = N
        dp_list = [0] * (end + 1)
        res = 0 
            
        if N > 0:
            dp_list[1] = 1
            
        for i in range(2, N + 1):
            dp_list[i] = dp_list[i - 1] + dp_list[i - 2]
            
        res = dp_list[-1]
        
        return res   
    
#        res = 0
#        first_value = 0
#        second_value = 1
#        
#        if not N:
#            
#            return res
#     
#        for i in range(2, N + 1):
#            # temp = first_value
#            # first_value = second_value
#            # second_value += temp
#            first_value, second_value = second_value, first_value + second_value
#
#        res = second_value
#        
#        return res
