# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import collections

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        
        value_list = collections.deque([startUrl])
        hostname_value = 'http://' + startUrl.split('/')[2]
        value_dict = set(value_list)
        res = []
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                url = value_list.popleft()
            
                for sub_url in htmlParser.getUrls(url):
                    if not sub_url in value_dict and hostname_value in sub_url:
                        value_list.append(sub_url)
                        value_dict.add(sub_url)
        
        res = list(value_dict)
        
        return res