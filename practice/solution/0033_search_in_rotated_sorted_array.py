class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums) - 1
        res = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                res = mid
                
                return res
            
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