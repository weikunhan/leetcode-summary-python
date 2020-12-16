class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        value_set = set(nums)
        res = 0
        
        for value in value_set:
            if not value - 1 in value_set:
                temp_value = value + 1
                
                while temp_value in value_set:
                    temp_value += 1
                    
                res = max(res, temp_value - value)
                
        return res