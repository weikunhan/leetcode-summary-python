import collections

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row_value_dict = collections.defaultdict(set)
        col_value_dict = collections.defaultdict(set)
        box_value_dict = collections.defaultdict(set)
        res = False
         
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in row_value_dict[i]:
                    
                    return res
                else:
                    row_value_dict[i].add(board[i][j])
                    
                if board[i][j] in col_value_dict[j]:
                    
                    return res
                else:
                    col_value_dict[j].add(board[i][j])
                    
                if board[i][j] in box_value_dict[(i // 3, j // 3)]:
                    
                    return res
                else:
                    box_value_dict[(i // 3, j // 3)].add(board[i][j])
                    
        res = True
        
        return res