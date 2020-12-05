# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low = 1
        high = n
        res = 0 

        while low < high:
            mid = (low + high) // 2

            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid
                
        res = low

        return res