class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        self.helper(0, len(nums) - 1, nums)
        self.helper(0, k - 1, nums)
        self.helper(k, len(nums) - 1, nums)
    
    def helper(self, start, end, nums):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1