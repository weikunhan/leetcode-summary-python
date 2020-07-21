class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        value_list = sorted(nums)
        res = []
        
        for i in range(len(value_list)):
            if i > 0 and value_list[i] == value_list[i - 1]:
                continue
                
            for j in range(i + 1, len(value_list)):
                left = j + 1
                right = len(value_list) - 1
                
                if j > i + 1 and value_list[j] == value_list[j - 1]:
                    continue
                    
                while left < right:
                    sum_value = value_list[i] + value_list[j] + value_list[left] + value_list[right]
                    
                    if sum_value == target:
                        res.append([value_list[i], value_list[j], value_list[left], value_list[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and value_list[left] == value_list[left - 1]:
                            left +=1
                            
                        while left < right and value_list[right] == value_list[right + 1]:
                            right -= 1
                    elif sum_value > target:
                        right -= 1
                    else:
                        left += 1
                        
        return res