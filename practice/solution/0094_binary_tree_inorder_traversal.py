# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.res = []

        self.inorder(root)

        return self.res

    def inorder(self, root):
        if not root:

            return

        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)