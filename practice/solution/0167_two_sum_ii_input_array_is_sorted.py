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
            
            if not numbers[i] in value_dict:
                value_dict[temp_value] = i
            else:
                res.append(value_dict[numbers[i]] + 1)
                res.append(i + 1)
                
                return res
                
        return res
