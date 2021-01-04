class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        odd_value_list = []
        even_value_list = []
        res = []
        
        for value in A:
            if value % 2 == 0:
                odd_value_list.append(value)
            else:
                even_value_list.append(value)
                
        res = odd_value_list + even_value_list
                
        return res