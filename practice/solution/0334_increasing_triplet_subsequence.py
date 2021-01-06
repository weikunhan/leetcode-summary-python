class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        first_value = sys.maxsize
        second_value = sys.maxsize
        res = False
        
        for num in nums:
            if num <= first_value:
                first_value = num
                continue
                
            if num <= second_value:
                second_value = num
                continue
            
            res = True
        
        return res