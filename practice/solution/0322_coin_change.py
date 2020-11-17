class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        end = amount
        dp_list = [end + 1] * (end + 1)
        dp_list[0] = 0
        res = -1
        
        for coin in coins:
            for i in range(coin, len(dp_list)):
                dp_list[i] = min(dp_list[i], dp_list[i - coin] + 1)
                
        if dp_list[-1] != end + 1:
            res = dp_list[-1]
        
        return  res