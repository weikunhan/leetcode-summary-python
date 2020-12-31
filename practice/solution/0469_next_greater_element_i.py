class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        value_dict = {}
        value_stack = []
        res = [-1] * len(nums1)
        
        for num in nums2:
            while value_stack and value_stack[-1] < num:
                temp_value = value_stack.pop()
                value_dict[temp_value] = num
                
            value_stack.append(num)
            
        for i in range(len(nums1)):
            if nums1[i] in value_dict:
                res[i] = value_dict[nums1[i]]
                
        return res
                