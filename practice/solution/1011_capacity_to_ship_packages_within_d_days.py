class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        
        low = max(weights)
        high = sum(weights)
        res = 0
        
        while low < high:
            count = 1
            sum_value = 0
            mid = (low + high) // 2
            
            for weight in weights:
                sum_value += weight
                
                if sum_value > mid:
                    sum_value = weight
                    count += 1
                    
            if count > D:
                low = mid + 1
            else:
                high = mid
                
        res = low
        
        return res