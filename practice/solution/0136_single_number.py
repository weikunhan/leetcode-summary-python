class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        value_dict = set()
        res = 0
        
        for value in nums:
            if value in value_dict:
                value_dict.remove(value)
            else:
                value_dict.add(value)
             
        for key in value_dict: 
            res = key
        
        return res

#        res = 0
#       
#       for num in nums:
#           res ^= num
#           
#        return res