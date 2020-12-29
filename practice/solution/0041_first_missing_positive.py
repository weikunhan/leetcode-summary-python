class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        
        for i in range(len(nums)):
            while nums[i] >= 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                # temp = nums[nums[i] - 1]
                # nums[nums[i] - 1] = nums[i]
                # nums[i] = temp
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res = i + 1
                
                return res
            
        res = len(nums) + 1
        
        return res
                