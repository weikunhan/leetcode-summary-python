class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        sum_value = 0
        res = sys.maxsize
        
        while right < len(nums):
            temp_value = nums[right]
            sum_value += temp_value

            while sum_value >= s and left < len(nums):
                res = min(res, right - left + 1)
                sum_value -= nums[left]
                left += 1
                
            right += 1
            
        if res == sys.maxsize:
            res = 0
            
        return res