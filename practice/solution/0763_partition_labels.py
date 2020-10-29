class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        value_dict = {}
        right = 0
        left = 0
        res = []
        
        for i in range(len(S)):
            value_dict[S[i]] = i
            
        for i in range(len(S)):
            right = max(right, value_dict[S[i]])
            
            if right == i:
                res.append(right - left + 1)
                left = i + 1
                
        return res