class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        value_dict = {}
        res = []
        
        for i in range(len(numbers)):
            temp_value = target - numbers[i]
            
            if numbers[i] in value_dict:
                res = [value_dict[numbers[i]] + 1, i + 1]
                
                return res
            else:
                value_dict[temp_value] = i
                
        return res

