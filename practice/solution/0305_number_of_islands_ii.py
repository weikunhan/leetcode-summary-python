class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        self.parent_value_dict = {}
        visit_value_dict = set()
        count = 0
        self.res = []
        
        for position in positions:
            i, j = position
            
            if not (i, j) in visit_value_dict:
                visit_value_dict.add((i, j))
                self.parent_value_dict[(i, j)] = (i, j)
                count += 1
                
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (a, b) in visit_value_dict:
                        if self.find((a, b)) != self.find((i, j)):
                            count -= 1
                            
                        self.union((a, b), (i, j))

            self.res.append(count)
        
        return self.res
    
    def find(self, x):
        if x != self.parent_value_dict[x]:
            self.parent_value_dict[x] = self.find(self.parent_value_dict[x])
            
        return self.parent_value_dict[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent_value_dict[root_x] = root_y 