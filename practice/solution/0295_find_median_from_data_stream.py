import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.min_value_pq = []
        self.max_value_pq = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        temp_value = heapq.heappushpop(self.min_value_pq, num)
        heapq.heappush(self.max_value_pq, -temp_value)
        
        if len(self.max_value_pq) > len(self.min_value_pq):
            temp_value = heapq.heappop(self.max_value_pq)
            heapq.heappush(self.min_value_pq, -temp_value)
            
    def findMedian(self):
        """
        :rtype: float
        """
        
        temp_value = 0
        
        if len(self.max_value_pq) < len(self.min_value_pq):
            temp_value = self.min_value_pq[0] / 1.0
        else:
            temp_value = (self.min_value_pq[0] - self.max_value_pq[0]) / 2.0
            
        return temp_value
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()