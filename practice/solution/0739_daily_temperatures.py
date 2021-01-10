class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        value_stack = []
        res = [0] * len(T)
        
        for i in range(len(T)):
            while value_stack and T[value_stack[-1]] < T[i]:
                temp_value = value_stack.pop()
                res[temp_value] = i - temp_value
            
            value_stack.append(i)

        return res