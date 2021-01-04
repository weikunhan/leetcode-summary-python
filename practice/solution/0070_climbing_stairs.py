class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        end = n
        dp_list = [0] * end
        res = 0 
        
        if n > 0:
            dp_list[0] = 1
            
        if n > 1:
            dp_list[1] = 2
            
        for i in range(2, n):
            dp_list[i] = dp_list[i - 1] + dp_list[i - 2]
            
        res = dp_list[-1]
        
        return res 

#        res = 0
#        first_value = 1
#        second_value = 2
#        
#        if not n:
#        
#            return res
#        
#        if n == 1:
#            res = first_value
#            
#            return res
#        
#        for i in range(2, n):
#            # temp = first_value
#            # first_value = second_value
#            # second_value += temp
#            first_value, second_value = second_value, first_value + second_value
#
#        res = second_value
#        
#        return res