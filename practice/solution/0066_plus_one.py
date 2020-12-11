class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        res = digits
        
        for i in reversed(range(len(digits))):
            if res[i] < 9:
                res[i] += 1
                
                return res
            else:
                res[i] = 0
                
        if not res[0]:
            res.insert(0, 1)
            
        return res
        