import collections

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        value_list = collections.deque([(start)])
        value_dict = set([start])
        res = False
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                step = value_list.popleft()
                
                if not arr[step]:
                    res = True
                    
                    return res
                    
                for i in [step + arr[step], step - arr[step]]:
                    if 0 <= i and i < len(arr) and not i in value_dict:
                        value_list.append(i)
                        value_dict.add(i)
                                   
        return res