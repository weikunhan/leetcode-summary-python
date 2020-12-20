class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        self.res = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, 0, word)

        return self.res
    
    def dfs(self, row, col, board, start, word):
        if start == len(word):
            self.res = True
        
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or self.res or board[row][col] != word[start]:
            
            return
        
        temp_value = board[row][col]
        board[row][col] = '#'
        self.dfs(row + 1, col, board, start + 1, word)
        self.dfs(row, col + 1, board, start + 1, word)
        self.dfs(row - 1, col, board, start + 1, word)
        self.dfs(row, col - 1, board, start + 1, word)
        board[row][col] = temp_value