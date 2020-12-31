class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        
        self.max_value = n
        self.row_value_list = [0] * n
        self.col_value_list = [0] * n
        self.diagonal_value = 0
        self.antidiagonal_value = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        
        temp_value = 0
        sign = 0
        
        if player == 1:
            sign = 1
        else:
            sign = -1
            
        self.row_value_list[row] += sign
        self.col_value_list[col] += sign
        
        if row == col:
            self.diagonal_value += sign
            
        if row == self.max_value - col - 1:
            self.antidiagonal_value += sign
            
        if abs(self.row_value_list[row]) == self.max_value or abs(self.col_value_list[col]) == self.max_value or abs(self.diagonal_value) == self.max_value or abs(self.antidiagonal_value) == self.max_value:
            temp_value = player
            
        return temp_value


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)