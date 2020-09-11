class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        res = False
        
        for i in range(1, len(flowerbed) - 1):
        	if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
        		flowerbed[i] = 1
        		count += 1
                
        if count >= n:
            res = True
            
        return res 