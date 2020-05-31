class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.word = []

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        value_trie = TrieNode()
        res = []
        
        for product in sorted(products):
            temp_root = value_trie
            
            for char in product:
                if not char in temp_root.next:
                    temp_root.next[char] = TrieNode()
                    
                temp_root = temp_root.next[char]
                
                if len(temp_root.word) < 3:
                    temp_root.word.append(product)
                        
        temp_root = value_trie
        
        for char in searchWord:
            if not char in temp_root.next:
                res += [[]] * (len(searchWord) - len(res))
                
                return res
            
            temp_root = temp_root.next[char]
            res.append(temp_root.word)
            
        return res