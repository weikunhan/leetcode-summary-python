class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        value_list = [0] + flowerbed + [0]
        res = False
        
        for i in range(1, len(value_list) - 1):
        	if value_list[i - 1] == value_list[i] == value_list[i + 1] == 0:
        		value_list[i] = 1
        		count += 1
                
        if count >= n:
            res = True
            
        return res 