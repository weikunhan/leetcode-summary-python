# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        self.value_list = []
        self.preorder_serialize(root)
        temp_value = ' '.join(self.value_list)
        
        return temp_value
    
    def preorder_serialize(self, root):
        if not root:
            self.value_list.append('#')
            
            return 
        
        self.value_list.append(str(root.val))
        self.preorder_serialize(root.left)
        self.preorder_serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        self.count = 0
        temp_value = self.preorder_deserialize(data.split(' '))
        
        return temp_value
    
    def preorder_deserialize(self, value_list):
        temp_value = value_list[self.count]
        self.count += 1
        
        if temp_value == '#':
            
            return 
        
        root = TreeNode(temp_value)
        root.left = self.preorder_deserialize(value_list)
        root.right = self.preorder_deserialize(value_list)
        
        return root    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans