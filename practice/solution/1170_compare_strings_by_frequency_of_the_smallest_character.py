class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        self.value_list = []
        self.res = []
        
        for word in words:
            self.value_list.append(word.count(min(word)))
        
        self.value_list = sorted(self.value_list)
        
        for query in queries:
            temp_value = self.helper(query.count(min(query)) + 1)
            self.res.append(len(self.value_list) - temp_value)
            
        return self.res   
        
    def helper(self, target):
        low = 0
        high = len(self.value_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if self.value_list[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low