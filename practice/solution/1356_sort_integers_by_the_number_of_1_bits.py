class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        res = sorted(arr, key=lambda x: (bin(x).count('1'), x))
        #res = sorted(arr, key=lambda x: (self.helper(x).count('1'), x))
        
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
#
#    def helper(self, num):
#        temp_value = ''
#        
#        for i in range(32):
#            temp_value += str((num >> i) & 1)
#            
#        return temp_value