import collections

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        value_dict = collections.defaultdict(list)
        res = []
        
        for path in paths:
            temp_list = path.split()
            temp_value = temp_list[0]
            
            for data in temp_list[1:]:
                index_value = data.index('(')
                value_dict[data[index_value + 1:-1]].append(temp_value + '/' + data[:index_value])
                
        for key, value in value_dict.items():
            if len(value) > 1:
                res.append(value)

        return res