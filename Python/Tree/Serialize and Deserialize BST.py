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
        s = []
        if root == None:
            return 'None'
        stack= [root]
        while stack:
            temp = stack.pop()
            if temp ==None:
                s.append('None')
            else:
                s.append(str(temp.val))
                stack.append(temp.right)
                stack.append(temp.left)
        return ','.join(s)
                    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(l):
            if l[0]=='None':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = helper(l)
            root.right = helper(l)
            return root
        d = data.split(',')
        root = helper(d)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


