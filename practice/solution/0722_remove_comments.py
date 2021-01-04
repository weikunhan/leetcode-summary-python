class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        
        sign = 1
        temp_value = ''
        res = []
        
        for line in source:
            count = 0
            
            while count < len(line):
                if sign and count < len(line) - 1 and line[count:count + 2] == '/*':
                    sign = 0
                    count += 2
                    continue
                    
                if not sign and count < len(line) - 1 and line[count:count + 2] == '*/':
                    sign = 1
                    count += 2
                    continue
                    
                if sign and line[count:count + 2] == '//':
                    break
                    
                if sign:
                    temp_value += line[count]
                    
                count += 1
            
            if temp_value and sign:
                res.append(temp_value)
                temp_value = ''
            
        return res