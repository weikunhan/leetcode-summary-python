class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.a_value_stack = []
        self.b_value_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        
        self.a_value_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
        temp_value = None
        
        if self.b_value_stack:
            temp_value = self.b_value_stack.pop()
        else:
            while self.a_value_stack:
                self.b_value_stack.append(self.a_value_stack.pop())
                
            temp_value = self.b_value_stack.pop()
        
        return temp_value

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

        temp_value = None
        
        if self.b_value_stack:
            temp_value = self.b_value_stack[-1]
        else:
            while self.a_value_stack:
                self.b_value_stack.append(self.a_value_stack.pop())
                
            temp_value = self.b_value_stack[-1]
        
        return temp_value

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        
        if not self.a_value_stack and not self.b_value_stack:
            
            return True
            
        return False
    
    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()