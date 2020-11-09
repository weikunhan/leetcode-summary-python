class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_trie = TrieNode()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        temp_root = self.value_trie
        
        for char in word:
            if not char in temp_root.next:
                
                return False
                
            temp_root = temp_root.next[char]
        
        if temp_root.word:
            
            return True
        else:
            
            return False
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        temp_root = self.value_trie
        
        for char in prefix:
            if not char in temp_root.next:
                
                return False
                
            temp_root = temp_root.next[char]
            
        return True

    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)