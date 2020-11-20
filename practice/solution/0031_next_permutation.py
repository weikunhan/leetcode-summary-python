class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        right = len(nums) - 1
        left = len(nums) - 1
        
        while left > 0 and nums[left - 1] >= nums[left]:
            left -= 1
            
        if left == 0:
            nums.reverse()
            
            return 
        
        while nums[left - 1] >= nums[right]:
            right -= 1
            
        # temp_value = nums[right]
        # nums[right] = nums[left - 1]
        # nums[left - 1] = temp_value
        nums[left - 1], nums[right] = nums[right], nums[left - 1] 
        right = len(nums) - 1
        
        while left < right:
            # temp_value = nums[right]
            # nums[right] = nums[left]
            # nums[left] = temp_value
            nums[left], nums[right] = nums[right], nums[left] 
            left += 1
            right -= 1