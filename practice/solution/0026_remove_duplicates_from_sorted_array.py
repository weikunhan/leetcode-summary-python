class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        res = 0
        
        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
            
            # temp = nums[right]
            # nums[right] =  nums[left]
            # nums[left] = temp
            nums[right], nums[left] = nums[left], nums[right]     
            right += 1
        
        res = left + 1
        
        return res