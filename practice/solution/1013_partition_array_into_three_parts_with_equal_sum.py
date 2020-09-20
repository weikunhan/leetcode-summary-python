class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        temp_value = sum(A)
        target_value = temp_value // 3
        sum_value = 0
        count = 0
        res = False
        
        if temp_value % 3: 
            
            return res

        for num in A:
            sum_value += num
            
            if sum_value == target_value:
                sum_value = 0
                count += 1
                
        if count >= 3:
            res = True
            
        return res