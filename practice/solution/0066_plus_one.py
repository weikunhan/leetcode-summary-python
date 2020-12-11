class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        res = digits
        
        for i in reversed(range(len(res))):
            if res[i] < 9:
                res[i] += 1
                
                return res
            else:
                res[i] = 0
                
        if res[0] == 0:
            res.insert(0, 1)
            
        return res
                         