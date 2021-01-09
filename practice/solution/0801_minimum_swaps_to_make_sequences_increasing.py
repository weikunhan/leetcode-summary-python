class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        end = len(A)
        dp_list = [[sys.maxsize, sys.maxsize] for _ in range(end)]
        dp_list[0][0] = 0
        dp_list[0][1] = 1
        res = 0
        
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp_list[i][0] = dp_list[i - 1][0]
                dp_list[i][1] = dp_list[i - 1][1] + 1
                
            if B[i] > A[i - 1] and A[i] > B[i - 1]:
                dp_list[i][0] = min(dp_list[i][0], dp_list[i - 1][1])
                dp_list[i][1] = min(dp_list[i][1], dp_list[i - 1][0] + 1)
                
        res = min(dp_list[-1])
                
        return res