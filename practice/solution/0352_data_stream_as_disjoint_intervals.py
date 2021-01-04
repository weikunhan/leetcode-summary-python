import heapq

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_pq = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """

        heapq.heappush(self.value_pq, [val, val])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        
        temp_list = []
        
        if self.value_pq:
            temp_list = [heapq.heappop(self.value_pq)]

        while self.value_pq:
            start, end = heapq.heappop(self.value_pq)
            
            if temp_list[-1][1] + 1 >= start:
                temp_list[-1][1] = max(temp_list[-1][1], end)
            else:
                temp_list.append([start, end])

        for interval in temp_list:
            heapq.heappush(self.value_pq, interval)
        
        return temp_list

    
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()