class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        value_stack = []
        res = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                value_stack.append(asteroid)
            else:
                while value_stack and value_stack[-1] < abs(asteroid):
                    value_stack.pop()

                if not value_stack:
                    res.append(asteroid)
                    continue
                
                if value_stack[-1] == abs(asteroid):
                    value_stack.pop()

        res += value_stack
        
        return res