class RangeModule(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """    
        
        self.value_list = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        
        start = self.helper(left)
        end = self.helper(right + 1)
        
        if start % 2:
            start -= 1
            left = self.value_list[start]
            
        if end % 2:
            right = self.value_list[end]
            end += 1
        
        self.value_list = self.value_list[:start] + [left, right] + self.value_list[end:]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        start = self.helper(left + 1)
        end = self.helper(right)
        
        if start == end and start % 2:
            
            return True
		
        return False

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        
        temp_list = []
        start = self.helper(left)
        end = self.helper(right + 1)

        if start % 2:
            start -= 1
            temp_list.append(self.value_list[start])
            temp_list.append(left)
            
        if end % 2:
            temp_list.append(right)
            temp_list.append(self.value_list[end])
            end += 1
			
        self.value_list = self.value_list[:start] + temp_list + self.value_list[end:]
        
    def helper(self, target):
        low = 0
        high = len(self.value_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if self.value_list[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)