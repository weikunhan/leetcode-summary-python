class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        value_list = arr
        res = [0] * len(arr)
        
        while res != value_list:
            for i in range(len(value_list)):
                res[i] = value_list[i]
            
            for i in range(1, len(value_list) - 1):
                if res[i - 1] < res[i] > res[i + 1]:
                    value_list[i] -= 1
                
                if res[i - 1] > res[i] < res[i + 1]:
                    value_list[i] += 1
                    
        return res
