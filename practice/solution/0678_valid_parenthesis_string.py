class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        min_value = 0
        max_value = 0
        res = False

        for char in s:
            if char == '(':
                min_value += 1
                max_value += 1
            elif char == ')':
                min_value = max(min_value - 1, 0)
                max_value -= 1
            else:
                min_value = max(min_value - 1, 0)
                max_value += 1

            if max_value < 0:

                return res

        if not min_value:
            res = True

        return res