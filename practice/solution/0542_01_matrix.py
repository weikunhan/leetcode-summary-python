import collections

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        value_list = collections.deque()
        res = matrix
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    value_list.append((i, j))
                    
                res[i][j] *= -1
                    
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                i, j = value_list.popleft()
                
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a >= 0 and a < len(res) and b >= 0 and b < len(res[0]) and res[a][b] < 0:
                        res[a][b] = res[i][j] + 1
                        value_list.append((a, b))
                        
        return res