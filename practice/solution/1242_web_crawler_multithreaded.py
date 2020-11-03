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
import threading

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        
        self.value_list = collections.deque([startUrl])
        self.hostname_value = 'http://' + startUrl.split('/')[2]
        self.work_value = 10
        self.thread_lock = threading.Lock()
        self.value_dict = set(self.value_list)
        self.res = []
        
        while self.value_list:
            temp_value = len(self.value_list)
            temp_list = []
            count = 0
            
            for _ in range(temp_value):
                url = self.value_list.popleft()
                thread = threading.Thread(target=self.helper, args=(url, htmlParser))
                temp_list.append(thread)
                count += 1
                
                if count == self.work_value:
                    self.executor(temp_list)
                    count = 0
                    temp_list = []
                    
            if temp_list:
                self.executor(temp_list)
        
        self.res = list(self.value_dict)
        
        return self.res
                
    def helper(self, url, htmlParser):
        for sub_url in htmlParser.getUrls(url):
            if not sub_url in self.value_dict and self.hostname_value in sub_url:
                self.thread_lock.acquire()
                self.value_list.append(sub_url)
                self.value_dict.add(sub_url)
                self.thread_lock.release()
                
    def executor(self, thread_value_list):
        for thread in thread_value_list:
            thread.start()

        for thread in thread_value_list:
            thread.join()