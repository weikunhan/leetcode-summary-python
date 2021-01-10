class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_dict = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        
        if message in self.value_dict:
            if timestamp < self.value_dict[message]:
                
                return False
        
        self.value_dict[message] = timestamp + 10
        
        return True
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)