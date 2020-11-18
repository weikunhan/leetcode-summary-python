class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    
        left = 0
        right = 0
        res = 0
        
        while right < len(nums):
            if nums[right] != val:
                # temp = nums[right]
                # nums[right] =  nums[left]
                # nums[left] = temp
                nums[right], nums[left] = nums[left], nums[right]
                left += 1                
        
            right += 1

        res = left
        
        return res