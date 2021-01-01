import collections

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        value_dict = collections.Counter(nums1)
        res = []
        
        for num in nums2:
            if value_dict[num] > 0:
                res.append(num)
                value_dict[num] = 0
        
        return res
        