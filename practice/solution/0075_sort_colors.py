class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        right = len(nums) - 1
        count = 0

        while count <= right:
            if nums[count] == 0:
                # temp = nums[left]
                # nums[left] = nums[count]
                # nums[count] = temp
                nums[left], nums[count] = nums[count], nums[left]
                left += 1
                count += 1
            elif nums[count] == 1:
                count += 1
            else:
                # temp = nums[count]
                # nums[count] = nums[right]
                # nums[right] = temp
                nums[count], nums[right] = nums[right], nums[count]
                right -= 1 