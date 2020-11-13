class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        value_list = path.split('/')
        value_stack = []
        res = '/'

        for path in value_list:
            if path and path != '.':
                if path == '..':
                    if value_stack:
                        value_stack.pop()
                else:
                    value_stack.append(path)

        res += '/'.join(value_stack)

        return res
                    
