class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        end = n
        dp_list = [0] * n 
        dp_list[0] = 1
        first_value = 0
        second_value = 0
        third_value = 0
        res = 0
        
        for i in range(1, n):
            two_value = dp_list[first_value] * 2
            three_value = dp_list[second_value] * 3
            five_value = dp_list[third_value] * 5
            temp_value = min(min(two_value, three_value), five_value)
            
            if two_value == temp_value:
                first_value += 1
                
            if three_value == temp_value:
                second_value += 1
                
            if five_value == temp_value:
                third_value += 1
                
            dp_list[i] = temp_value
            
        res = dp_list[-1]
        
        return res