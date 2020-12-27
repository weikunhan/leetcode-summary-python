# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        
        self.value_stack = []
        
        while root:
            self.value_stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        
        temp_root = self.value_stack.pop()
        temp_value = temp_root.val
        temp_root = temp_root.right
        
        while temp_root:
            self.value_stack.append(temp_root)
            temp_root = temp_root.left
            
        return temp_value        

    def hasNext(self):
        """
        :rtype: bool
        """
        
        if self.value_stack:
            
            return True
        else:
            
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()