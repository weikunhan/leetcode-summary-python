import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.value_dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        temp_value = -1
        
        if key in self.value_dict:
            temp_value = self.value_dict[key]
            self.value_dict.pop(key)
            self.value_dict[key] = temp_value
        
        return temp_value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.value_dict:
            self.value_dict.pop(key)
            self.value_dict[key] = value
        else:    
            if len(self.value_dict) == self.capacity:
                self.value_dict.popitem(last=False)
                
            self.value_dict[key] = value
                
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)