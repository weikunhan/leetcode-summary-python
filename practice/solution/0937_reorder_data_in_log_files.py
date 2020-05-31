class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        data_value_list = []
        letter_value_list = []
        res = []
        
        for log in logs:
            if log.split(' ')[1].isdigit():
                data_value_list.append(log)
            else:
                letter_value_list.append(log)
                
        letter_value_list = sorted(letter_value_list, key=lambda x:x.split(' ')[0])
        letter_value_list = sorted(letter_value_list, key=lambda x:x.split(' ')[1:])
        res = letter_value_list + data_value_list
        
        return res