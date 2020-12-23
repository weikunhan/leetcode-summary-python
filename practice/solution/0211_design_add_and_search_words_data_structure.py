class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_trie = TrieNode()
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        
        temp_root = self.value_trie
        
        for char in word:
            if not char in temp_root.next:
                temp_root.next[char] = TrieNode()

            temp_root = temp_root.next[char]
            
        temp_root.word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        self.temp_value = False
        temp_root = self.value_trie
        
        self.helper(temp_root, word)
        
        return self.temp_value
            
    def helper(self, root, word):
        if not word:
            if root.word:
                self.temp_value = True
                
            return 
        
        if word[0] == ".":
            for key, value in root.next.items():
                self.helper(value, word[1:])
                
        if word[0] in root.next:
            self.helper(root.next[word[0]], word[1:])

            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)