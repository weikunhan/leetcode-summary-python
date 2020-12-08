class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = len(s.strip().split(' ')[-1])

        return res