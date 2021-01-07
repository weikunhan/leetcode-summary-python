class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        row = click[0]
        col = click[1]
        
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            self.dfs(row, col, board)
            
        return board
        
    def dfs(self, row, col, board):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != 'E':
            
            return
        
        count = 0
        
        for a, b in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1), (row + 1, col + 1), (row - 1, col + 1), (row + 1, col - 1)]:
            if a >= 0 and a < len(board) and b >= 0 and b < len(board[0]) and board[a][b] == 'M':
                count += 1
        
        if not count:
            board[row][col] = 'B'
        else:
            board[row][col] = str(count)
            
            return
        
        self.dfs(row - 1, col, board)
        self.dfs(row + 1, col, board)
        self.dfs(row, col - 1, board)
        self.dfs(row, col + 1, board)
        self.dfs(row - 1, col + 1, board)
        self.dfs(row + 1, col - 1, board)
        self.dfs(row + 1, col + 1, board)
        self.dfs(row - 1, col - 1, board)
        