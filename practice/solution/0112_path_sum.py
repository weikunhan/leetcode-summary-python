# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        self.res = False

        self.preorder(root, sum)

        return self.res

    def preorder(self, root, target):
        if not root:

            return 

        if not root.left and not root.right and root.val == target:
            self.res = True

        self.preorder(root.left, target - root.val)
        self.preorder(root.right, target - root.val)