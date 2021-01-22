class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        left = 0
        right = 0
        res = 0
        
        while right < len(A):
            temp_value = A[right]
            K -= 1 - temp_value
            
            if K < 0:
                K += 1 - A[left]
                left += 1
                
            res = max(res, right - left + 1)
            right += 1
            
        return res
                