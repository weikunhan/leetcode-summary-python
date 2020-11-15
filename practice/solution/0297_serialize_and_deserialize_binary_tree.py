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
        
        value_list = []
        
        self.preorder_serialize(root, value_list)
        temp_value = ' '.join(value_list)
        
        return temp_value
    
    def preorder_serialize(self, root, value_list):
        if not root:
            value_list.append('#')
            
            return 
        
        value_list.append(str(root.val))
        self.preorder_serialize(root.left, value_list)
        self.preorder_serialize(root.right, value_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        self.count = 0
        value_list = data.split(' ')
        
        temp_value = self.preorder_deserialize(value_list)
        
        return temp_value
    
    def preorder_deserialize(self, value_list):
        temp_value = value_list[self.count]
        self.count += 1
        
        if temp_value == '#':
            
            return None
        
        root = TreeNode(temp_value)
        root.left = self.preorder_deserialize(value_list)
        root.right = self.preorder_deserialize(value_list)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))