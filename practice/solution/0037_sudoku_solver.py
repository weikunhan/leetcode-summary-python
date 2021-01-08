import collections

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.row_value_dict = collections.defaultdict(set)
        self.col_value_dict = collections.defaultdict(set)
        self.box_value_dict = collections.defaultdict(set)
                
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                self.row_value_dict[i].add(board[i][j])
                self.col_value_dict[j].add(board[i][j])
                self.box_value_dict[(i // 3, j // 3)].add(board[i][j])
        
        self.dfs(board)
                        
    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                    
                for char in '123456789':
                    if self.helper(i, j, char): 
                        board[i][j] = char
                        self.row_value_dict[i].add(board[i][j])
                        self.col_value_dict[j].add(board[i][j])
                        self.box_value_dict[(i // 3, j // 3)].add(board[i][j])
                    
                        if self.dfs(board):
                            
                            return True
                        
                        board[i][j] = '.'
                        self.row_value_dict[i].remove(char)
                        self.col_value_dict[j].remove(char)
                        self.box_value_dict[(i // 3, j // 3)].remove(char)             
                    
                return False

        return True
        
    def helper(self, row, col, char):
        if char in self.row_value_dict[row]:

            return False

        if char in self.col_value_dict[col]:

            return False

        if char in self.box_value_dict[(row // 3, col // 3)]:

            return False

        return True