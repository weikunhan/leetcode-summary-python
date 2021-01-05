import threading
import collections

class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.value_list = collections.deque()
        self.thread_lock = threading.Lock()
        self.dequeue_value = threading.Semaphore(capacity)
        self.enqueue_value = threading.Semaphore(0)

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        
        self.dequeue_value.acquire()
        self.thread_lock.acquire()
        self.value_list.append(element)
        self.thread_lock.release()
        self.enqueue_value.release()

    def dequeue(self):
        """
        :rtype: int
        """
           
        self.enqueue_value.acquire()
        self.thread_lock.acquire()
        temp_value = self.value_list.popleft()
        self.thread_lock.release()
        self.dequeue_value.release()     
        
        return temp_value

    def size(self):
        """
        :rtype: int
        """
        
        temp_value = len(self.value_list)
        
        return temp_value