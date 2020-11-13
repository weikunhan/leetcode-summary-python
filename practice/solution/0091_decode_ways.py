class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        end = len(s)
        dp_list = [0] * (end + 1)
        dp_list[0] = 1
        res = 0

        if s[0] != '0':
            dp_list[1] = 1

        for i in range(2, len(dp_list)):
            if s[i - 1:i] != '0':
                dp_list[i] += dp_list[i - 1]

            if 10 <= int(s[i - 2:i]) <= 26:
                dp_list[i] += dp_list[i - 2]

        res = dp_list[-1]

        return res