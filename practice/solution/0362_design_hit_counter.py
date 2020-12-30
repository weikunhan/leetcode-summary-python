import collections

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_list = collections.deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        
        self.value_list.append(timestamp)
            
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        
        while self.value_list and timestamp - self.value_list[0] >= 300: 
            self.value_list.popleft()
            
        temp_value = len(self.value_list)
        
        return temp_value
        

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)