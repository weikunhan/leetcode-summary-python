import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.value_list = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        
        return self.value_list

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        
        temp_list = []
        
        for num in self.value_list:
            temp_list.append(num)
        
        for i in reversed(range(len(temp_list))):
            index_value = random.randint(0, i)
            # temp =  temp_list[i]
            # temp_list[i] = temp_list[index_value]
            # temp_list[index_value] = temp
            temp_list[i], temp_list[index_value] = temp_list[index_value], temp_list[i]    
        
        return temp_list


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()