import collections

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.frequency_value_dict = {}
        self.recently_value_dict = collections.defaultdict(collections.OrderedDict)
        self.capacity = capacity
        self.min_frequency = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        temp_value = -1
        
        if key in self.frequency_value_dict:
            temp_value, frequency = self.frequency_value_dict[key]
            self.frequency_value_dict[key] = (temp_value, frequency + 1)
            self.recently_value_dict[frequency].pop(key)
            self.recently_value_dict[frequency + 1][key] = None
            
            if not self.recently_value_dict[frequency] and frequency == self.min_frequency:
                self.min_frequency = frequency + 1
    
        return temp_value
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if not self.capacity:
            
            return 
        
        if key in self.frequency_value_dict:
            self.get(key)
            _, frequency = self.frequency_value_dict[key]
            self.frequency_value_dict[key] = (value, frequency)
        else:
            if len(self.frequency_value_dict) == self.capacity:
                temp_key, _ = self.recently_value_dict[self.min_frequency].popitem(last=False)
                self.frequency_value_dict.pop(temp_key)
                
            self.frequency_value_dict[key] = (value, 1)
            self.recently_value_dict[1][key] = None
            self.min_frequency = 1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)