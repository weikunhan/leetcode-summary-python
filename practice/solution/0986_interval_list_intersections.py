class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        left = 0
        right = 0
        res = []
        
        while left < len(A) and right < len(B):
            start = max(A[left][0], B[right][0])
            end = min(A[left][1], B[right][1])
            
            if start <= end:
                res.append([start, end])
                
            if A[left][1] < B[right][1]:
                left += 1
            else:
                right += 1
                
        return res