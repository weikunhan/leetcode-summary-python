class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        value_dict = {}
        res = []
        
        for i in range(len(nums)):
            temp_value = target - nums[i]
            
            if nums[i] in value_dict:
                res = [value_dict[nums[i]], i]
                
                return res
            else:
                value_dict[temp_value] = i
                
        return res