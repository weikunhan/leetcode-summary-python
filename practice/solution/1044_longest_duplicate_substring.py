class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        self.value_list = []
        self.max_value = sys.maxsize
        low = 0
        high = len(S)
        count = 0
        self.res = ''

        for char in S:
            self.value_list.append(ord(char) - ord('a'))
        
        while low < high:
            mid = (low + high) // 2
            temp_value = self.helper(mid)
            
            if temp_value:
                low = mid + 1
                count = temp_value
            else:
                high = mid
            
        self.res = S[count:count + low - 1]
        
        return self.res
    
    def helper(self, start):
        value_dict = set()
        base_value = 26 ** start % self.max_value
        temp_value = 0
        sum_value = 0
        
        #for i in range(start):
        #    sum_value = (sum_value * 26 + self.value_list[i]) % self.max_value
        sum_value = reduce(lambda x, y:(x * 26 + y) % self.max_value, self.value_list[:start], 0)
        value_dict.add(sum_value)
        
        for i in range(start, len(self.value_list)):
            sum_value = (sum_value * 26 + self.value_list[i] - self.value_list[i - start] * base_value) % self.max_value
            
            if sum_value in value_dict:
                temp_value = i - start + 1
                
                return temp_value
            
            value_dict.add(sum_value)
        
        return temp_value