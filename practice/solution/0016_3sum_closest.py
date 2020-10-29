class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        value_list = sorted(nums)
        temp_value = sys.maxsize
        res = 0
        
        for i in range(len(value_list)):
            left = i + 1
            right = len(value_list) - 1
            
            if i >= 1 and value_list[i] == value_list[i - 1]:
                continue
                
            while left < right:
                sum_value = value_list[i] + value_list[left] + value_list[right]
                
                if sum_value - target == 0:
                    res = target
                    
                    return res
                elif sum_value - target > 0:
                    right -= 1
                else:
                    left += 1
                    
                if abs(sum_value - target) < abs(temp_value):
                    temp_value = sum_value - target
                    res = sum_value
                
        return res
                    
        