class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        low = 0
        high = len(nums) - 1
        res = False
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                res = True
                
                return res
            
            while low < mid and nums[low] == nums[mid]:
                low += 1
            
            if nums[low] > nums[mid]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                        
        return res