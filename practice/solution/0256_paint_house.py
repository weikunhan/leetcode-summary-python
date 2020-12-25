class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        dp_list = costs
        res = 0
        
        if not costs:
            
            return res
        
        for i in range(1, len(costs)):
            for j in range(3):
                dp_list[i][j] += min(dp_list[i - 1][(j + 1) % 3], dp_list[i - 1][(j + 2) % 3])
        
        
        res = min(min(dp_list[-1][0], dp_list[-1][1]), dp_list[-1][2])
            
        return res