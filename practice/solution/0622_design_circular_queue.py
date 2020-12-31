class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        
        self.max_value = k
        self.size_value = 0
        self.front_value = 0
        self.last_value = -1
        self.value_list = [1] * k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        
        if self.size_value != self.max_value:
            self.last_value = (self.last_value + 1) % self.max_value
            self.value_list[self.last_value] = value
            self.size_value += 1
            
            return True
        else: 
            
            return False        

    def deQueue(self):
        """
        :rtype: bool
        """
 
        if self.size_value:
            self.front_value = (self.front_value + 1) % self.max_value
            self.size_value -= 1
            
            return True
        else: 
            
            return False    

    def Front(self):
        """
        :rtype: int
        """
        
        temp_value = -1
        
        if self.size_value:     
            temp_value = self.value_list[self.front_value]
            
        return temp_value

    def Rear(self):
        """
        :rtype: int
        """
        
        temp_value = -1
        
        if self.size_value:
            temp_value = self.value_list[self.last_value]
            
        return temp_value

    def isEmpty(self):
        """
        :rtype: bool
        """
        
        if not self.size_value:
            
            return True
        else:
            
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        
        if self.size_value == self.max_value:
            
            return True
        else:
            
            return False
    

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()