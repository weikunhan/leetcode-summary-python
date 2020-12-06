class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        a_value_dict = {}
        b_value_dict = {}
        res = []
        
        for i in range(len(list1)):
            a_value_dict[list1[i]] = i
            
        for i in range(len(list2)):
            if list2[i] in a_value_dict:
                b_value_dict[list2[i]] = i + a_value_dict[list2[i]]
        
        for key, value in b_value_dict.items():
            if value == min(b_value_dict.values()):
                res.append(key)
                
        return res
