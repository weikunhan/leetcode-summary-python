class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = bin(n).count('1')
        #res = self.helper(n).count('1') 
        
        return res
    
#    def helper(self, num):
#        if num < 1:
#            temp_value = str(num)
#            
#            return temp_value
#        
#        carry, remainder = divmod(num, 2)
#        temp_value = self.helper(carry) + str(remainder)
#        
#       return temp_value

#    def helper(self, num):
#        temp_value = ''
#        
#        for i in range(32):
#            temp_value += str((num >> i) & 1)
#            
#        return temp_value