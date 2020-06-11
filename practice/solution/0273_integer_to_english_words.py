class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        self.ones_value_list = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
                                "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens_value_list = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands_value_list = ["","Thousand","Million","Billion"]
        self.res = ''
        
        if num == 0:
            self.res = 'Zero'
            
            return self.res
        
        for i in range(len(self.thousands_value_list)):
            carry, remainder = divmod(num, 1000)
            
            if remainder != 0:
                self.res = self.helper(remainder) + self.thousands_value_list[i] + ' ' + self.res
                
            num = carry
            
        self.res = self.res.strip(' ')
            
        return self.res
            
    def helper(self, num):
        temp_value = ''
        
        if num == 0:
            
            return temp_value
        
        if num < 20:
            temp_value = self.ones_value_list[num] + ' '
            
            return temp_value
        
        if num < 100:
            temp_value = self.tens_value_list[num / 10] + ' ' + self.helper(num % 10)
            
            return temp_value
        
        if num < 1000:
            temp_value = self.ones_value_list[num / 100] + ' Hundred ' + self.helper(num % 100)
            
            return temp_value
