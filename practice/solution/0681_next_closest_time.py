class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        hour_value, minute_value = time.split(':')
        number_value_list = sorted(set(hour_value + minute_value))
        time_value_list = []
        res = ''
        
        for a in number_value_list:
            for b in number_value_list:
                time_value_list.append(a + b)

        index_value = time_value_list.index(minute_value)
        
        if index_value + 1 < len(time_value_list) and int(time_value_list[index_value + 1]) < 60:
            res = hour_value + ':' + time_value_list[index_value + 1]
            
            return res
        
        index_value = time_value_list.index(hour_value)
                            
        if index_value + 1 < len(time_value_list) and int(time_value_list[index_value + 1]) < 24:
            res = time_value_list[index_value + 1] + ':' + time_value_list[0]
            
            return res
        
        res = time_value_list[0] + ':' + time_value_list[0]
        
        return res
