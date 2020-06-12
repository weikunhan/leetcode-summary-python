class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        
        res = False
        
        while tx >= sx and ty >= sy:
            if tx > ty:
                if ty == sy:
                    if not (tx - sx) % ty:
                        res = True
                        
                        return res
                    else:
                        
                        return res
                
                tx %= ty
            else:
                if tx == sx:
                    if not (ty - sy) % tx:
                        res = True
                        
                        return res
                    else:
                        
                        return res
                
                ty %= tx
        
        if ty == sy and tx == sx:
            res = True
        
        return res