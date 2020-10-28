class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        value_dict = set()
        res = False
        
        for num in nums:
            if not num in value_dict:
                value_dict.add(num)
            else:
                res = True
                
                return res
            
        return res