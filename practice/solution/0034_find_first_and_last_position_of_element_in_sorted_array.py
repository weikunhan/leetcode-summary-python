class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left_value = 0
        right_value = 0
        self.res = [-1, -1]
    
        left_value = self.helper(nums, target)
        right_value = self.helper(nums, target + 1) - 1
        
        if left_value == len(nums) or right_value == len(nums):
            
            return self.res
        
        if nums[left_value] == nums[right_value] == target:
            self.res = [left_value, right_value]
            
            return self.res
        
        return self.res

    def helper(self, nums, target):
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low