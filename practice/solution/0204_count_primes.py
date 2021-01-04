class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        end = n
        dp_list =  [True] * end
        res = 0
        
        if n < 2:
            
            return res
        
        dp_list[0] = False
        dp_list[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if dp_list[i]:
                for j in range(i * i, n, i):
                    dp_list[j] = False

        res = sum(dp_list)
        
        return res