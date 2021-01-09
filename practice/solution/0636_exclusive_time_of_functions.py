class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
        value_stack = []
        start = 0
        res = [0] * n
        
        for log in logs:
            id_value, state_value, time_value = log.split(':')
            
            if state_value == 'start':
                if value_stack:
                    res[value_stack[-1]] += int(time_value) - start
                    
                value_stack.append(int(id_value))
                start = int(time_value)    
            else:
                temp_value = value_stack.pop()
                res[temp_value] += int(time_value) - start + 1
                start = int(time_value) + 1
                
        return res