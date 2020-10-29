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
            a_low = -sys.maxsize - 1
            b_low = -sys.maxsize - 1
            a_high = sys.maxsize
            b_high = sys.maxsize
            
            if a_mid:
                a_low = nums1[a_mid - 1]
                
            if b_mid:
                b_low = nums2[b_mid - 1]
            
            if a_mid != len(nums1):
                a_high = nums1[a_mid]
                
            if b_mid != len(nums2):
                b_high = nums2[b_mid]
            
            if a_low > b_high:
                high = a_mid - 1
            elif b_low > a_high:
                low = a_mid + 1
            else:
                if (len(nums1) + len(nums2)) % 2:
                    res = min(a_high, b_high) / 1.0
                else:
                    res = (max(a_low, b_low) + min(a_high, b_high)) / 2.0
                
                return res
            
        return res