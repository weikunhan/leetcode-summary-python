class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        a_value_dict = {}
        b_value_dict = {}
        res = [[0] * len(B[0]) for _ in range(len(A))]
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    a_value_dict[(i, j)] = A[i][j]
                    
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]:
                    b_value_dict[(i, j)] = B[i][j]
               
        for (row_a, col_a), value_a in a_value_dict.items():
            for (row_b, col_b), value_b in b_value_dict.items():
                if col_a == row_b: 
                    res[row_a][col_b] += value_a * value_b
        
        return res