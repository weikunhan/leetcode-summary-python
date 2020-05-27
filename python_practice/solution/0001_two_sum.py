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
            
            if not nums[i] in value_dict:
                value_dict[temp_value] = i
            else:
                res.append(value_dict[nums[i]])
                res.append(i)
                
                return res
        
        return res