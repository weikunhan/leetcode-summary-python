import collections

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        visit_value_dict = set()
        data_value_dict = set(stones)
        value_list = collections.deque([(0, 0)])
        res = False
        
        while value_list:
            temp_value = len(value_list)
            
            for _  in range(temp_value):
                stone, cost = value_list.popleft()
                
                if stone == stones[-1]:
                    res = True
                    
                    return res
                
                for i in [cost - 1, cost, cost + 1]:
                    if i > 0 and stone + i <= stones[-1] and stone + i in data_value_dict and not (stone + i, i) in visit_value_dict:
                        value_list.append((stone + i, i))
                        visit_value_dict.add((stone + i, i))
                        
        return res