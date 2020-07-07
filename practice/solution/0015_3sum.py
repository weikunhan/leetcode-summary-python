class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        value_list = sorted(nums)
        res = []
        
        for i in range(len(value_list)):
            left = i + 1
            right = len(value_list) - 1
            
            if i > 0 and value_list[i] == value_list[i - 1]:
                continue
                
            while left < right:
                sum_value = value_list[i] + value_list[left] + value_list[right]
                
                if not sum_value:
                    res.append([value_list[i], value_list[left], value_list[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and value_list[left] == value_list[left - 1]:
                        left += 1

                    while left < right and value_list[right] == value_list[right + 1]:
                        right -= 1
                elif sum_value < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res