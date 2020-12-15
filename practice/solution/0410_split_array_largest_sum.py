class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
        low = max(nums)
        high = sum(nums)
        res = 0
        
        while low < high:
            count = 1
            sum_value = 0
            mid = (low + high) // 2
            
            for num in nums:
                sum_value += num
                
                if sum_value > mid:
                    sum_value = num
                    count += 1
                    
            if count > m:
                low = mid + 1
            else:
                high = mid
                
        res = low
        
        return res