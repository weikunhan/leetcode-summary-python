import collections

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        self.parent_value_dict = {}
        self.mapping_value_dict = {}
        self.merging_value_dict = collections.defaultdict(list)
        self.res = []
        
        for acount in accounts:
            name_value = acount[0]
            
            for email in acount[1:]:
                if not email in self.parent_value_dict:
                    self.parent_value_dict[email] = email
                    
                self.union(email, acount[1])
                self.mapping_value_dict[email] = name_value
                
        for key, value in self.parent_value_dict.items():
            temp_value = self.find(key)
            self.merging_value_dict[temp_value].append(key)
            
        for key, value in self.merging_value_dict.items():
            name_value = self.mapping_value_dict[key]
            self.res.append([name_value] + sorted(value))
            
        return self.res
                
    def find(self, x):
        if x != self.parent_value_dict[x]:
            self.parent_value_dict[x] = self.find(self.parent_value_dict[x])
            
        return self.parent_value_dict[x]
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent_value_dict[root_x] = root_y