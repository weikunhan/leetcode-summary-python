class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not board[i][j]:
                    if self.helper(i, j, board) == 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 0
                else:
                    if self.helper(i, j, board) < 2 or self.helper(i, j, board) > 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = 1
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                
                if board[i][j] == 3:
                    board[i][j] = 0
                    
    def helper(self, row, col, board):
        count = 0
        
        for a, b in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1), (row + 1, col + 1), (row - 1, col + 1), (row + 1, col - 1)]:
            if a >= 0 and a < len(board) and b >= 0 and b < len(board[0]):
                count += board[a][b] % 2
                
        return count