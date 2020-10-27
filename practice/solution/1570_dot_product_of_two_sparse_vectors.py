class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.value_dict = {}
        
        for i in range(len(nums)):
            if nums[i]: 
                self.value_dict[i] = nums[i]        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        nums1 = self.value_dict
        nums2 = vec.value_dict
        res = 0
        
        if len(nums1) > len(nums2):
            #temp = nums1
            #nums1 = nums2
            #nums2 = temp
            nums1, nums2 = nums2,  nums1
            
        for key, value in nums1.items():
            if key in nums2:
                res += value * nums2[key]
                
        return res
            
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)