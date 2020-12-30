class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low = 0
        high = len(nums) - 1
        res = 0
        
        while low < high:
            mid = 2 * ((low + high) // 4)
            
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
                
        res = nums[low]
        
        return res