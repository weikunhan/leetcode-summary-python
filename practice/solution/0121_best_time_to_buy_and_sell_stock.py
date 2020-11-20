class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        end = len(prices)
        dp_list = [0] * end
        res = 0
        
        if not prices:
            
            return res
        
        temp_value = prices[0]
            
        for i in range(1, len(dp_list)):
            dp_list[i] = max(dp_list[i - 1], prices[i] - temp_value)
            temp_value = min(temp_value, prices[i])
        
        res = dp_list[-1]

        return res