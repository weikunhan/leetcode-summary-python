class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        value_list = [lower - 1] + nums + [upper + 1]
        res = []
            
        for i in range(len(value_list) - 1):
            if value_list[i + 1] - value_list[i] == 2:
                res.append(str(value_list[i] + 1))
            
            if value_list[i + 1] - value_list[i] > 2:
                res.append(str(value_list[i] + 1) + '->' + str(value_list[i + 1] - 1))
            
        return res