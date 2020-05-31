import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.small_value_pq = []
        self.large_value_pq = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        temp_value = heapq.heappushpop(self.large_value_pq, num)
        heapq.heappush(self.small_value_pq, -temp_value)
        
        if len(self.small_value_pq) > len(self.large_value_pq):
            temp_value = heapq.heappop(self.small_value_pq)
            heapq.heappush(self.large_value_pq, -temp_value)

    def findMedian(self):
        """
        :rtype: float
        """
        
        temp_value = 1.0
        
        if len(self.small_value_pq) < len(self.large_value_pq):
            temp_value = self.large_value_pq[0] / temp_value
        else:
            temp_value = (self.large_value_pq[0] - self.small_value_pq[0]) / 2.0
            
        return temp_value


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()