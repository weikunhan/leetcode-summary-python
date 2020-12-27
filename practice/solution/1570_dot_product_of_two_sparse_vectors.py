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

        a_value_dict = self.value_dict
        b_value_dict = vec.value_dict
        temp_value = 0
        
        if len(a_value_dict) > len(b_value_dict):
            #temp = a_value_dict
            #a_value_dict = b_value_dict
            #b_value_dict = temp
            b_value_dict, a_value_dict = a_value_dict,  b_value_dict
            
        for key, value in a_value_dict.items():
            if key in b_value_dict:
                temp_value += value * b_value_dict[key]
                
        return temp_value
            
            
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)