# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        
        self.peek_value = None
        self.iterator_value = iterator
        
        if self.iterator_value.hasNext():
            self.peek_value = self.iterator_value.next()
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        
        return self.peek_value

    def next(self):
        """
        :rtype: int
        """
        
        temp_value = self.peek_value
        self.peek_value = None
        
        if self.iterator_value.hasNext():
            self.peek_value = self.iterator_value.next()
            
        return temp_value
            
    def hasNext(self):
        """
        :rtype: bool
        """
        
        if self.peek_value:
            
            return True
        else:
            
            return False


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].