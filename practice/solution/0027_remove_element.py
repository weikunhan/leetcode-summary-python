class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    
        count = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else: 
                nums[i - count] = nums[i];
        
        res = len(nums) - count
        
        return res