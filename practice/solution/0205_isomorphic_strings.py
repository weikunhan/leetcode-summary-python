class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        a_value_dict = set(s)
        b_value_dict = set(t)
        c_value_dict = set()
        res = False
        
        for pair in zip(s, t):
            c_value_dict.add(pair)

        if len(a_value_dict) == len(b_value_dict) == len(c_value_dict):
            res = True

        return res