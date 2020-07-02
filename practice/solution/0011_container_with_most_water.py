class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        res = 0
        
        while left < right:
            temp_value = min(height[left], height[right])
            res = max(res, temp_value * (right - left))
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return res