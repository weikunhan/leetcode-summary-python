class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        value_dict = set(nums)
        res = 0
        
        for value in value_dict:
            if not value - 1 in value_dict:
                temp_value = value + 1
                
                while temp_value in value_dict:
                    temp_value += 1
                    
                res = max(res, temp_value - value)
                
        return res