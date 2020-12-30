class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        self.value_list = []
        self.res = 0
        
        for num in nums:
            temp_value = self.helper(num)
            
            if temp_value == len(self.value_list):
                self.value_list.append(num)
            else:
                self.value_list[temp_value] = num
                
        self.res = len(self.value_list)
        
        return self.res
    
    def helper(self, target):
        low = 0
        high = len(self.value_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if self.value_list[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low