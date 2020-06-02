class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.word = ''

class FileSystem(object):

    def __init__(self):
        
        self.value_trie = TrieNode()

    def insert(self, path):
        temp_root = self.value_trie
        
        for char in path.split('/')[1:]:
            if not char in temp_root.next:
                temp_root.next[char] = TrieNode()
                
            temp_root = temp_root.next[char]
            
        return temp_root
    
    def search(self, path):
        temp_root = self.value_trie
        
        for char in path.split('/')[1:]:
            if not char in temp_root.next:
                
                return temp_root
                
            temp_root = temp_root.next[char]
            
        return temp_root
    
    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        
        temp_list = [path.split('/')[-1]]
        temp_root = self.search(path)
        
        if temp_root.word:
            
            return temp_list
        
        temp_list = sorted(temp_root.next.keys())
        
        return temp_list

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        
        self.insert(path)

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        
        temp_root = self.insert(filePath)
        temp_root.word += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        
        temp_root = self.search(filePath)
        temp_value = temp_root.word
        
        return temp_value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)