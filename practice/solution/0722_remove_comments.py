class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        
        sign = -1
        temp_value = ''
        res = []
        
        for code in source:
            count = 0
            
            while count < len(code):
                if sign == -1:
                    if count < len(code) - 1 and code[count:count + 2] == '//':
                        break
                    
                    if count < len(code) - 1 and code[count:count + 2] == '/*':
                        sign = 1
                        count += 2
                        continue
                    
                    temp_value += code[count]
                else:
                    if count < len(code) - 1 and code[count:count + 2] == '*/':
                        sign = -1
                        count = count + 2
                        continue
        
                count += 1
                       
            if sign == -1 and temp_value:
                res.append(temp_value)
                temp_value = ''
                
        return res