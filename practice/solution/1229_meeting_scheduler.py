class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        
        a_value_list = sorted(slots1)
        b_value_list = sorted(slots2)
        left = 0
        right = 0
        res = []
        
        while left < len(slots1) and right < len(slots2):
            start = max(a_value_list[left][0], b_value_list[right][0])
            end = min(a_value_list[left][1], b_value_list[right][1])
            
            if start + duration <= end:
                res = [start, start + duration]
                
                return res
            
            if a_value_list[left][1] < b_value_list[right][1]:
                left += 1
            else:
                right += 1
                
        return res
        