import collections
import heapq

class Leaderboard(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_dict = collections.Counter()

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        
        self.value_dict[playerId] += score
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        
        temp_value = 0
        temp_list = heapq.nlargest(K, self.value_dict, key=lambda x:self.value_dict[x])
        
        for num in temp_list:
            temp_value += self.value_dict[num]
            
        return temp_value

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        
        self.value_dict[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)