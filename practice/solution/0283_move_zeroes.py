class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        right = 0
        
        while right < len(nums):
            if nums[right]:
                # temp =  nums[right]
                # nums[right] =  nums[left]
                # nums[left] = temp
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                
            right += 1
        