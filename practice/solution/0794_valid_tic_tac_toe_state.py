class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        
        x_value = False
        o_value = False
        row_value_list = [0] * 3
        col_value_list = [0] * 3
        diagonal_value = 0
        anti_diagonal_value = 0
        sign = 0
        trun_value = 0
        res = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ' ':
                    continue
                elif board[i][j] == 'X':
                    sign = 1
                else:
                    sign = -1
                
                trun_value += sign
                row_value_list[i] += sign
                col_value_list[j] += sign

                if i == j:
                    diagonal_value += sign

                if j == 3 - i - 1:
                    anti_diagonal_value += sign
                
        if 3 in set(row_value_list) or 3 in set(col_value_list) or diagonal_value == 3 or anti_diagonal_value == 3:
             x_value = True
                
        if -3 in set(row_value_list) or -3 in set(col_value_list) or diagonal_value == -3 or anti_diagonal_value == -3:
             o_value = True   
        
        if (x_value and o_value) or (trun_value != 1 and trun_value !=0 ) or (x_value and trun_value == 0 ) or (o_value and trun_value == 1):
            
            return res
        
        res = True
        
        return res