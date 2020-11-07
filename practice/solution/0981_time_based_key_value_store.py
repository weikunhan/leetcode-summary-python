import collections

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_dict = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        
        self.value_dict[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        
        temp_list = self.value_dict[key]
        temp_value = ''
        low = 0
        high = len(temp_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if temp_list[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid
                
        if high:
            temp_value = temp_list[high - 1][1]
            
        return temp_value
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)