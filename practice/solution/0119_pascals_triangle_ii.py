class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        end = rowIndex
        dp_list = [0] * (end + 1)
        dp_list[0] = 1
        res = []
        
        for i in range(1, rowIndex + 1):
            for j in reversed(range(1, i + 1)):
                dp_list[j] += dp_list[j - 1]
                
        res = dp_list
        
        return res