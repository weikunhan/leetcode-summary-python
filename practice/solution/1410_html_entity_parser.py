class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        
        a_value_dict = {'&quot;': '"', '&apos;': "'", '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        b_value_dict = {'&amp;': '&'}
        res = text
        
        for key, value in a_value_dict.items():
            res = re.sub(key, value, res)
            
        for key, value in b_value_dict.items():
            res = re.sub(key, value, res)        
            
        return res   