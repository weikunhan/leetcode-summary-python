""" User-Based Recommendation System

Design user-based recommendation system based on gived two APIs that can do:

getFriends (Person p)-> [Person] returns all friends of person
getVideos (Person p)-> [Video] returns all the favorite videos of the person
Recommend a video to a person, the algorithm is to find all the videos his friends 
like and sort by the number of likes.

Here, we can simplify the APIs as two Dict[String, List[String]], one is userVideos 
with user names as keys and a list of all the video that the user has likes.
Another is userFriends with user names as keys and a list of all this friend. 
The task is to return a Dict[String, List[String]],where the key is a user name 
and the value is a list Top K recommendation video based on his friend, if there 
is the same number of likes, then the video with the lower alphabetical order comes first.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-580122-1-1.html

Time complexity: O(n^3)
Space complexity: O(n)

Example 1:
Input:
userVideos = {
    "David": ["Django Unchained", "Fight Club", "Inception"],
    "Emma": ["Predators", "Forrest Gump", "Alien"],
    "Jack": ["Fight Club", "The Shawshank Redemption", "Life Is Beautiful", 
             "Back to the Future", "Forrest Gump", "Alien"]}
userFriends = {
    "David": ["Emma", "Jack"],
    "Emma": ["David"],
    "Jack": ["David"]}
k = 3
Output:
{
    'Emma': ['Django Unchained', 'Fight Club', 'Inception'],
    'Jack': ['Django Unchained', 'Inception'],
    'David': ['Alien', 'Forrest Gump', 'Back to the Future']
}

Example 2:
Input:
userVideos = {
    "David": ["Django Unchained", "Fight Club", "Inception"],
    "Emma": ["Predators", "Forrest Gump", "Alien"],
    "Jack": ["Fight Club", "The Shawshank Redemption", "Life Is Beautiful", "Back to the Future", "Forrest Gump", "Alien"]}
userFriends = {
    "David": [],
    "Emma": [],
    "Jack": []}
k = 3
Output:
{
    'Emma': [],
    'Jack': [],
    'David': []
}

Example 3
Input:
userVideos = {
    "David": ["Django Unchained", "Fight Club", "Inception"],
    "Emma": ["Predators", "Forrest Gump", "Alien"],
    "Jack": ["Fight Club", "The Shawshank Redemption", "Life Is Beautiful", "Back to the Future", "Forrest Gump", "Alien"]}
userFriends = {
    "David": ["Emma", "Jack"],
    "Emma": ["David"],
    "Jack": ["David"]}
k = 1
Output:
{
    'Emma': ['Django Unchained'],
    'Jack': ['Django Unchained'],
    'David': ['Alien']}
}
"""

import heapq
import collections

class Solution(object):
    def user_based_recommendation_system(self, userVideos, userFriends, k):
        """
        :type userSongs: Dict[List[str]]
        :type songGenres: Dict[List[str]]
        :rtype: Dict[List[str]]
        """

        res = {}

        for user, friend_value_list in userFriends.items():
            video_value_dict = set(userVideos[user])
            count_value_dict = collections.Counter()

            for friend in friend_value_list:
                for video in userVideos[friend]:
                    if not video in video_value_dict:
                        count_value_dict[video] += 1

            res[user] = heapq.nsmallest(k, count_value_dict, key=lambda x:(-count_value_dict[x], x))

        return res

def main():
    userVideos = { 
        "David": ["Django Unchained", "Fight Club", "Inception"],
        "Emma": ["Predators", "Forrest Gump", "Alien"],
        "Jack": ["Fight Club", "The Shawshank Redemption", "Life Is Beautiful", 
                 "Back to the Future", "Forrest Gump", "Alien"]}
    userFriends = { 
        "David": ["Emma", "Jack"],
        "Emma": ["David"], 
        "Jack": ["David"]}
    k = 3
    solution = Solution()
    res = solution.user_based_recommendation_system(userVideos, userFriends, k)
    print(res)

if __name__ == "__main__": 
    main()