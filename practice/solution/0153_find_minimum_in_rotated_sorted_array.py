class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        low = 0
        high = len(nums) - 1
        res = 0
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
        res = nums[low]
        
        return res