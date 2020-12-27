class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        end = amount
        dp_list = [0] * (end + 1)
        dp_list[0] = 1
        res = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp_list[i] += dp_list[i - coin]
                    
        res = dp_list[-1]
        
        return res