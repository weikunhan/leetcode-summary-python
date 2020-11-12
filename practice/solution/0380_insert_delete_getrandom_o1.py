import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_list = []
        self.value_dict = {}
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if not val in self.value_dict:
            self.value_list.append(val)
            self.value_dict[val] = len(self.value_list) - 1
            
            return True
        
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val in self.value_dict:
            index_value = self.value_dict[val]
            self.value_dict[self.value_list[-1]] = index_value
            self.value_list[index_value] = self.value_list[-1]
            self.value_list.pop()
            self.value_dict.pop(val)
            
            return True
        
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        temp_value = self.value_list[random.randint(0, len(self.value_list) - 1)]
        
        return temp_value


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()