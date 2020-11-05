class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        self.value_list = [ord(x) - ord('a') for x in S]
        self.max_length = sys.maxsize
        low = 0
        high = len(S)
        count = 0
        res = ''
        
        while low < high:
            mid = (low + high) // 2
            temp_value = self.helper(mid)
            
            if temp_value:
                low = mid + 1
                count = temp_value
            else:
                high = mid
                
        res = S[count:count + low - 1]
            
        return res
        
    def helper(self, length):
        value_dict = set()
        base_value = 26 ** length % self.max_length
        temp_value = 0
        
        sum_value = reduce(lambda x, y:(x * 26 + y) % self.max_length, self.value_list[:length], 0)
        value_dict.add(sum_value)
        
        for i in range(length, len(self.value_list)):
            sum_value = (sum_value * 26 + self.value_list[i] - self.value_list[i - length] * base_value) % self.max_length
            
            if sum_value in value_dict:
                temp_value = i - length + 1
                
                return temp_value
            
            value_dict.add(sum_value)
            
        return temp_value
        