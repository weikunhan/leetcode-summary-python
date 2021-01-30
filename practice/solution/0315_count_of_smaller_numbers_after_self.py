class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        value_dict = {}
        max_value = len(set(nums)) + 1
        value_list = [0] * (max_value)
        count = 1
        res = []
        
        for key in sorted(set(nums)):
            value_dict[key] = count
            count += 1

        for num in reversed(nums):
            sum_value = 0
            index_value = value_dict[num] - 1

            while index_value:
                sum_value += value_list[index_value]
                index_value -= (index_value & -index_value)
                
            res.append(sum_value)
            index_value = value_dict[num]
            
            while index_value < max_value:
                value_list[index_value] += 1
                index_value += (index_value & -index_value)
            
        res = res[::-1]
            
        return res