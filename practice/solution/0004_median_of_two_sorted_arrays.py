class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) > len(nums2):
            #temp = nums1
            #nums1 = nums2
            #nums2 = temp
            nums1, nums2 = nums2, nums1
        
        low = 0
        high = len(nums1)
        res = -1
        
        while low <= high:
            a_mid = (low + high) // 2
            b_mid = (len(nums1) + len(nums2)) // 2 - a_mid
            a_mid_left_value = -sys.maxsize - 1
            b_mid_left_value = -sys.maxsize - 1
            a_mid_right_value = sys.maxsize
            b_mid_right_value = sys.maxsize
            
            if a_mid:
                a_mid_left_value = nums1[a_mid - 1]
                
            if b_mid:
                b_mid_left_value = nums2[b_mid - 1]
            
            if a_mid != len(nums1):
                a_mid_right_value = nums1[a_mid]
                
            if b_mid != len(nums2):
                b_mid_right_value = nums2[b_mid]
            
            if a_mid_left_value > b_mid_right_value:
                high = a_mid - 1
            elif b_mid_left_value > a_mid_right_value:
                low = a_mid + 1
            else:
                if (len(nums1) + len(nums2)) % 2:
                    res = min(a_mid_right_value, b_mid_right_value) / 1.0
                else:
                    res = (max(a_mid_left_value, b_mid_left_value) + min(a_mid_right_value, b_mid_right_value)) / 2.0
                
                return res
            
        return res