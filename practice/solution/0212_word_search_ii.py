class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.word = False

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        self.value_trie = TrieNode()
        self.value_dict = set()
        self.res = []
        
        for word in words:
            temp_root = self.value_trie
            
            for char in word:
                if not char in temp_root.next:
                    temp_root.next[char] = TrieNode()
                    
                temp_root = temp_root.next[char]
                
            temp_root.word = True
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp_root = self.value_trie
                self.dfs(i, j, board, temp_root, [])
                
        self.res = list(self.value_dict)
        
        return self.res
    
    def dfs(self, row, col, board, value_trie, value_list):
        if value_trie.word:
            self.value_dict.add(''.join(value_list))
            value_trie.word = False
            
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or not board[row][col] in value_trie.next:
            
            return 
            
        temp_value = board[row][col]
        board[row][col] = '#'
        self.dfs(row + 1, col, board, value_trie.next[temp_value], value_list + [temp_value])
        self.dfs(row, col + 1, board, value_trie.next[temp_value], value_list + [temp_value])
        self.dfs(row - 1, col, board, value_trie.next[temp_value], value_list + [temp_value])
        self.dfs(row, col - 1, board, value_trie.next[temp_value], value_list + [temp_value])
        board[row][col] = temp_value
