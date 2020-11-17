import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        value_dict = collections.Counter(nums1)
        res = []

        for value in nums2:
            if value_dict[value] > 0:
                res.append(value)
                value_dict[value] -= 1

        return res