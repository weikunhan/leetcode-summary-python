class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        value_list = digits
        res = []
        
        for i in reversed(range(len(value_list))):
            if value_list[i] < 9:
                value_list[i] += 1
                res = value_list
                
                return res
            else:
                value_list[i] = 0
                
        if not value_list[0]:
            res = [1] + value_list
        else:
            res = value_list
            
        return res
        