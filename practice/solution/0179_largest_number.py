class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        value_list = []
        res = ''
        
        for num in nums:
            value_list.append(str(num))
            
        value_list = sorted(value_list, cmp=lambda x, y: cmp(x + y, y + x), reverse=True)
        
        res = ''.join(value_list)
        
        if not int(res):
            res = '0'
            
        return res
        