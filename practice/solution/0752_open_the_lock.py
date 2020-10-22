import collections

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        value_dict = set(deadends)
        value_list = collections.deque([('0000', 0)])
        visit_value_dict = {}
        res = -1
        
        if '0000' in value_dict:
            
            return res
        
        for i in range(10):
            visit_value_dict[str(i)] = [str((i + 1) % 10), str((i - 1) % 10)]
            
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                move, cost = value_list.popleft()
                
                if move == target:
                    res = cost
                    
                    return res
                
                for i in range(4):
                    a = move[:i] + visit_value_dict[move[i]][0] + move[i + 1:]
                    b = move[:i] + visit_value_dict[move[i]][1] + move[i + 1:]
                    
                    for new_move in [a, b]:
                        if not new_move in value_dict:
                            value_list.append((new_move, cost + 1))
                            value_dict.add(new_move)
                            
        return res