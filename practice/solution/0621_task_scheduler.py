import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        value_dict = collections.Counter(tasks)
        count = 0
        res = 0
        
        for key, value in value_dict.items():
            if value == max(value_dict.values()):
                count += 1
                
        temp_value = (max(value_dict.values()) - 1) * (n + 1) + count 
        res = max(len(tasks), temp_value)
        
        return res