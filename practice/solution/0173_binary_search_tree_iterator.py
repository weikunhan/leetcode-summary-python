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
        @return the next smallest number
        :rtype: int
        """
        
        root = self.value_stack.pop()
        temp_value = root.val
        root = root.right

        while root:
            self.value_stack.append(root)
            root = root.left

        return temp_value

    def hasNext(self):
        """
        @return whether we have a next smallest number
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