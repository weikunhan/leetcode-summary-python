import collections

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        self.res = 0
        
        self.res = self.helper(A, K) - self.helper(A, K - 1)
        
        return self.res
        
    def helper(self, A, max_value):
        value_dict = collections.Counter()
        left = 0
        right = 0
        count = 0
        
        while right < len(A):
            temp_value = A[right]
            value_dict[temp_value] += 1
            
            if value_dict[temp_value] == 1:
                max_value -= 1
            
            while max_value < 0:
                temp_value = A[left]
                value_dict[temp_value] -= 1
                
                if not value_dict[temp_value]:
                    max_value += 1
                
                left += 1
            
            count += right - left + 1
            right += 1
                    
        return count