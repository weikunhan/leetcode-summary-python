class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
     
        missing_value = nums[-1] - nums[0] + 1 - len(nums)
        temp_value = 0
        low = 0
        high = len(nums) - 1
        res = 0
        
        if k > missing_value:
            res = nums[-1] - missing_value + k
            
            return res
        
        while low <= high:
            mid = (low + high) // 2
            missing_value = nums[mid] - nums[temp_value] + 1 - (mid - temp_value + 1)
            
            if k > missing_value:
                temp_value = mid
                low = mid + 1
                k -= missing_value
            else:
                high = mid - 1
                
        res = nums[temp_value] + k        
                
        return res