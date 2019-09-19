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
        self.s=[]
        self.helper(root)
        return ','.join(self.s)
    
    def helper(self,root):
        if root is None:
            self.s.append('None')
        else:
            self.s.append(str(root.val))
            self.helper(root.left)
            self.helper(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l=data.split(',')
        root=self.dhelper(l)
        return root
    
    def dhelper(self,l):
        if l[0]=='None':
            l.pop(0)
            return None
        root=TreeNode(l[0])
        l.pop(0)
        root.left=self.dhelper(l)
        root.right=self.dhelper(l)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))