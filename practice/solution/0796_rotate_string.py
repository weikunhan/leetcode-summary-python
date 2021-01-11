class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        res = False
        
        if len(A) == len(B) and B in A + A:
            res = True
            
        return res