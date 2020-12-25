class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        sum_value = sum(stones)
        end = sum_value // 2
        dp_list = [0] * (end + 1)
        res = 0
        
        for stone in stones:
            for i in reversed(range(stone, sum_value // 2 + 1)):
                dp_list[i] = max(dp_list[i], dp_list[i - stone] + stone)
                
        res = sum_value - 2 * dp_list[-1]
        
        return res