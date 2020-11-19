class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        
        a_value_list = []
        b_value_list = []
        res = False
        
        for i in range(len(start)):
            if start[i] == 'L' or start[i] == 'R':
                a_value_list.append((start[i], i))
            
        for i in range(len(end)):
            if end[i] == 'L' or end[i] == 'R':
                b_value_list.append((end[i], i))
            
        if len(a_value_list) != len(b_value_list):
            
            return res
        
        for a, b in zip(a_value_list, b_value_list):
            if a[0] != b[0]:
                
                return res
            
            if a[0] == 'L':
                if a[1] < b[1]:
                    
                    return res
                
            if a[0] == 'R':
                if a[1] > b[1]:
                    
                    return res
                
        res = True
        
        return res