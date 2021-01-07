import collections
import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.data_value_dict = collections.defaultdict(list)
        self.user_value_dict = collections.defaultdict(set)
        self.count = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        
        self.data_value_dict[userId].append((self.count, tweetId))
        self.count -= 1
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        
        value_pq = []
        temp_dict = self.user_value_dict[userId]
        temp_dict.add(userId)
        count = 10
        temp_list = []
        
        for user in temp_dict:
            for data in self.data_value_dict[user]:
                heapq.heappush(value_pq, (data))
        
        while count and value_pq:
            temp_list.append(heapq.heappop(value_pq)[1])
            count -= 1
        
        return temp_list

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        
        self.user_value_dict[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        
        if followeeId in self.user_value_dict[followerId]:
            self.user_value_dict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)